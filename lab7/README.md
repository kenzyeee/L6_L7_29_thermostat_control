# Lab 7: Fuzz Testing

The module accepts text input for temperature setpoints, comma-separated sensor readings, and `HH:MM` schedule times. Inputs outside the documented formats are rejected with `TypeError` or `ValueError`, rather than failing unpredictably.

Run from this folder:

```bash
python -m pytest -q
```

Hypothesis generates ordinary text, empty strings, and `None` values for each parser, alongside examples that exercise valid Celsius/Fahrenheit, CSV, and time inputs.
