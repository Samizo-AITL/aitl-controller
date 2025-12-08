import pytest
from aitl_controller.pid import PID
from aitl_controller.fsm import FSM
from aitl_controller.llm import FakeLLM
from aitl_controller.controller import AITL


def test_controller_step_output_positive():
    pid = PID(1.0, 0.1, 0.01)
    fsm = FSM()
    llm = FakeLLM()
    ctl = AITL(pid, fsm, llm)

    u, state = ctl.step(1.0, 0.0, dt=0.1)

    assert u > 0.0
    assert state in (FSM.NORMAL, FSM.DISTURB, FSM.TUNE)


def test_controller_invalid_dt():
    pid = PID(1.0, 0.1, 0.01)
    fsm = FSM()
    llm = FakeLLM()
    ctl = AITL(pid, fsm, llm)

    with pytest.raises(ValueError):
        ctl.step(1.0, 0.0, dt=0)

    with pytest.raises(ValueError):
        ctl.step(1.0, 0.0, dt=-0.1)


def test_controller_state_transitions_and_tuning():
    """
    Test that:
    - Large error -> DISTURB
    - Smaller error -> TUNE
    - In TUNE state, LLM modifies PID gains
    """
    pid = PID(1.0, 0.1, 0.01)
    fsm = FSM()
    llm = FakeLLM()
    ctl = AITL(pid, fsm, llm)

    # Step 1: large error -> DISTURB
    _, state1 = ctl.step(2.0, 0.0, dt=0.1)
    assert state1 == FSM.DISTURB

    # Step 2: moderate error -> TUNE
    _, state2 = ctl.step(0.1, 0.0, dt=0.1)
    assert state2 == FSM.TUNE

    # Track PID gains before tuning
    kp_before = pid.kp
    kd_before = pid.kd

    # Step 3: still in TUNE -> LLM must tune PID
    _, state3 = ctl.step(0.1, 0.0, dt=0.1)
    assert state3 == FSM.TUNE

    # Gains must be changed
    assert pid.kp != kp_before
    assert pid.kd != kd_before


def test_controller_no_tuning_in_normal():
    """
    When state = NORMAL, LLM must NOT tune PID gains.
    """
    pid = PID(1.0, 0.1, 0.01)
    fsm = FSM()
    llm = FakeLLM()
    ctl = AITL(pid, fsm, llm)

    # Small error keeps FSM in NORMAL
    _, state = ctl.step(0.01, 0.0, dt=0.1)
    assert state == FSM.NORMAL

    kp_before = pid.kp
    kd_before = pid.kd

    # Another small error → still NORMAL
    ctl.step(0.01, 0.0, dt=0.1)

    # Gains must NOT change in NORMAL state
    assert pid.kp == kp_before
    assert pid.kd == kd_before
