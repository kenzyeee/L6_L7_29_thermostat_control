import pytest

from thermostat_control import energy_alert, hvac_action, target_temperature


@pytest.mark.parametrize(
    ("mode", "occupied", "hour", "expected"),
    [
        ("away", True, 7, 16),
        ("sleep", True, 5, 18),
        ("sleep", True, 6, 20),
        ("sleep", True, 21, 20),
        ("sleep", True, 22, 18),
        ("home", False, 7, 18),
        ("home", True, 5, 20),
        ("home", True, 6, 22),
        ("home", True, 8, 22),
        ("home", True, 9, 20),
        ("home", True, 16, 20),
        ("home", True, 17, 21),
        ("home", True, 21, 21),
        ("home", True, 22, 20),
    ],
)
def test_target_temperature_branches(mode, occupied, hour, expected):
    assert target_temperature(mode, occupied, hour) == expected


@pytest.mark.parametrize(
    ("current", "target", "outside", "expected"),
    [
        (20, 20, 0, "idle"),
        (20, 20.99, 0, "idle"),
        (20, 21, 4.99, "heat_boost"),
        (20, 21, 5, "heat"),
        (21, 20, 30, "cool"),
        (21, 20, 30.01, "cool_boost"),
    ],
)
def test_hvac_action_branches(current, target, outside, expected):
    assert hvac_action(current, target, outside) == expected


def test_energy_alert_empty_readings():
    assert energy_alert([], 10) == "ok"


@pytest.mark.parametrize(
    ("readings", "limit", "expected"),
    [
        ([10, 9, 10], 10, "ok"),
        ([11, 10, 9], 10, "warning"),
        ([11, 11, 9], 10, "critical"),
        ([11], 10, "critical"),
    ],
)
def test_energy_alert_threshold_branches(readings, limit, expected):
    assert energy_alert(readings, limit) == expected
