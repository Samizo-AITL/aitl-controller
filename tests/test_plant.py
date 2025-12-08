import pytest
from aitl_controller.plant import Plant


def test_plant_monotonic_response():
    plant = Plant(tau=1.0)

    x1 = plant.step(1.0, dt=0.1)
    x2 = plant.step(1.0, dt=0.1)

    # First-order lag should increase monotonically toward 1.0
    assert x2 > x1
    assert x2 < 1.0  # should not overshoot for first-order model


def test_plant_reset():
    plant = Plant()
    plant.step(1.0)
    plant.reset()

    assert plant.state == 0.0
    assert plant.x == 0.0


def test_plant_invalid_tau():
    with pytest.raises(ValueError):
        Plant(tau=0)

    with pytest.raises(ValueError):
        Plant(tau=-1.0)


def test_plant_invalid_dt():
    plant = Plant()

    with pytest.raises(ValueError):
        plant.step(1.0, dt=0)

    with pytest.raises(ValueError):
        plant.step(1.0, dt=-0.1)


def test_plant_state_property():
    plant = Plant()

    plant.step(1.0, dt=0.1)
    assert isinstance(plant.state, float)
    assert plant.state == plant.x
