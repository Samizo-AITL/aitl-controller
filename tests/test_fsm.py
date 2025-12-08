import pytest
from aitl_controller.fsm import FSM


def test_fsm_disturb_transition():
    fsm = FSM()

    # Large error -> DISTURB
    assert fsm.transition(2.0) == FSM.DISTURB
    assert fsm.state == FSM.DISTURB


def test_fsm_disturb_to_tune_transition():
    fsm = FSM()

    fsm.transition(2.0)  # -> DISTURB
    assert fsm.state == FSM.DISTURB

    # Error reduced but still above NORMAL threshold -> TUNE
    assert fsm.transition(0.1) == FSM.TUNE
    assert fsm.state == FSM.TUNE


def test_fsm_tune_to_normal_transition():
    fsm = FSM()

    fsm.transition(2.0)   # -> DISTURB
    fsm.transition(0.1)   # -> TUNE

    # Error sufficiently small -> NORMAL
    assert fsm.transition(0.01) == FSM.NORMAL
    assert fsm.state == FSM.NORMAL


def test_fsm_no_direct_disturb_to_normal():
    fsm = FSM()

    fsm.transition(2.0)  # -> DISTURB

    # Even if error is small enough for NORMAL threshold,
    # FSM must go DISTURB -> TUNE -> NORMAL, not directly.
    assert fsm.transition(0.01) == FSM.TUNE


def test_fsm_reset():
    fsm = FSM()

    fsm.transition(2.0)  # -> DISTURB
    fsm.reset()

    assert fsm.state == FSM.NORMAL


def test_fsm_invalid_error():
    fsm = FSM()

    with pytest.raises(ValueError):
        fsm.transition(None)
