from hypothesis import given, strategies as st
import pytest

from thermostat_control import average_temperature, parse_setpoint, schedule_slot


@given(st.one_of(st.text(), st.none()))
def test_parse_setpoint_fuzz_inputs_do_not_crash_unexpectedly(value):
    try:
        result = parse_setpoint(value)
    except (TypeError, ValueError):
        return
    assert isinstance(result, float)


@given(st.one_of(st.text(), st.none()))
def test_average_temperature_fuzz_inputs_do_not_crash_unexpectedly(value):
    try:
        result = average_temperature(value)
    except (TypeError, ValueError):
        return
    assert isinstance(result, float)


@given(st.one_of(st.text(), st.none()))
def test_schedule_slot_fuzz_inputs_do_not_crash_unexpectedly(value):
    try:
        result = schedule_slot(value)
    except (TypeError, ValueError):
        return
    assert result.startswith(("night ", "day "))


@pytest.mark.parametrize(("text", "expected"), [("21.5C", 21.5), ("70F", 21.1), (" -40 f ", -40.0)])
def test_parse_setpoint_valid_values(text, expected):
    assert parse_setpoint(text) == expected


@pytest.mark.parametrize("text", ["", "21", "C", "nanC", "infF", "20X"])
def test_parse_setpoint_rejects_malformed_or_nonfinite_values(text):
    with pytest.raises(ValueError):
        parse_setpoint(text)


def test_parse_setpoint_rejects_none():
    with pytest.raises(TypeError):
        parse_setpoint(None)


@pytest.mark.parametrize(("csv", "expected"), [("20,22", 21.0), (" 19.5, 20.5, 22 ", 20.666666666666668)])
def test_average_temperature_valid_values(csv, expected):
    assert average_temperature(csv) == pytest.approx(expected)


@pytest.mark.parametrize("csv", ["", ",", "20,", ",20", "20,nope", "nan", "inf"])
def test_average_temperature_rejects_malformed_or_nonfinite_values(csv):
    with pytest.raises(ValueError):
        average_temperature(csv)


def test_average_temperature_rejects_none():
    with pytest.raises(TypeError):
        average_temperature(None)


@pytest.mark.parametrize(("text", "expected"), [("05:07", "night 07"), ("6:00", "day 0"), ("23:59", "day 59")])
def test_schedule_slot_valid_values(text, expected):
    assert schedule_slot(text) == expected


@pytest.mark.parametrize("text", ["", "7", "24:00", "12:60", "-1:00", "12:3x", "1:2:3"])
def test_schedule_slot_rejects_malformed_or_out_of_range_values(text):
    with pytest.raises(ValueError):
        schedule_slot(text)


def test_schedule_slot_rejects_none():
    with pytest.raises(TypeError):
        schedule_slot(None)
