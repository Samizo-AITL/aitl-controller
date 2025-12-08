import pytest
from aitl_controller.pid import PID
from aitl_controller.llm import FakeLLM


def test_llm_gain_increase():
    pid = PID(1.0, 0.1, 0.01)
    llm = FakeLLM()

    llm.tune(pid, 1.0)  # Large error -> gain increases

    assert pid.kp == pytest.approx(1.0 * FakeLLM.KP_UP)
    assert pid.kd == pytest.approx(0.01 * FakeLLM.KD_UP)


def test_llm_gain_decrease():
    pid = PID(1.0, 0.1, 0.01)
    llm = FakeLLM()

    llm.tune(pid, 0.1)  # Small error -> fine decrease

    assert pid.kp == pytest.approx(1.0 * FakeLLM.KP_DOWN)
    assert pid.kd == pytest.approx(0.01 * FakeLLM.KD_DOWN)


def test_llm_gain_changes_in_sequence():
    pid = PID(1.0, 0.1, 0.01)
    llm = FakeLLM()

    # 1) Large error → up
    llm.tune(pid, 1.0)
    kp_after_up = pid.kp
    kd_after_up = pid.kd

    # 2) Small error → down
    llm.tune(pid, 0.1)

    assert pid.kp < kp_after_up
    assert pid.kd < kd_after_up


def test_llm_invalid_error():
    pid = PID(1.0, 0.1, 0.01)
    llm = FakeLLM()

    with pytest.raises(ValueError):
        llm.tune(pid, None)
