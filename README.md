# L6_L7_29 - Smart Thermostat Controller

Completed deliverables for Lab 6 (code and branch coverage) and Lab 7 (property-based fuzz testing).

## Project layout

- `lab6/` contains the Lab 6 controller and branch-focused pytest suite.
- `lab7/` contains the Lab 7 input parsers and Hypothesis fuzz tests.
- `requirements.txt` lists the test dependencies.

## Run

Install dependencies from the repository root:

```bash
python -m pip install -r requirements.txt
```

To inspect Lab 6 coverage:

```bash
python -m pytest lab6 --cov=thermostat_control --cov-branch --cov-report=term-missing
```

Run the Lab 6 suite from inside `lab6/` so pytest imports the correct module:

```bash
cd lab6
python -m pytest --cov=thermostat_control --cov-branch --cov-report=term-missing
```

Run Lab 7 from inside `lab7/`:

```bash
cd lab7
python -m pytest -q
```
