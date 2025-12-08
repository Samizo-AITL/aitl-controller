import pytest
from aitl_controller.pid import PID


def test_pid_basic_integration_growth():
    pid = PID(1.0, 0.1, 0.01)

    u1 = pid(1.0, dt=0.1)
    u2 = pid(1.0, dt=0.1)

    # Because of integration, u2 should be larger than u1
    assert u2 > u1


def test_pid_reset():
    pid = PID(1.0, 0.1, 0.01)

    pid(1.0, dt=0.1)
    pid.reset()

    assert pid.i == 0.0
    assert pid.prev_e == 0.0


def test_pid_derivative_computation():
    pid = PID(1.0, 0.1, 0.01)

    pid(1.0, dt=0.1)  # prev_e = 1.0
    u = pid(2.0, dt=0.1)

    # derivative term = (2 - 1) / 0.1 = 10
    # output contains kd * derivative = 0.01 * 10 = 0.1
    assert u > 0.1


def test_pid_gains_property():
    pid = PID(1.0, 0.1, 0.01)

    kp, ki, kd = pid.gains

    assert kp == 1.0
    assert ki == 0.1
    assert kd == 0.01


def test_pid_invalid_dt():
    pid = PID(1.0, 0.1, 0.01)

    with pytest.raises(ValueError):
        pid(1.0, dt=0.0)

    with pytest.raises(ValueError):
        pid(1.0, dt=-0.1)
