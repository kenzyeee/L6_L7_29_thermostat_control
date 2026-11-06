# Lab 6: Code and Branch Coverage

The thermostat functions are exercised across mode, time, occupancy, HVAC action, and energy alert branches.

Run from this folder:

```bash
python -m pytest --cov=thermostat_control --cov-branch --cov-report=term-missing
```

The tests target both outcomes of each decision and boundary values such as 6:00, 9:00, 17:00, 22:00, a one-degree HVAC difference, and the outside-temperature thresholds.
