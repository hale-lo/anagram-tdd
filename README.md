# anagram-tdd

An anagram identifier application, 

## Features

-

## Project structure

- `app.py` contains the command-line interface.
- `anagram.py` contains the tested anagram logic.
- `tests/` contains the unit tests.
- `.github/workflows/test.yml` contains the CI workflow.

## Run the application

```powershell
python app.py
```

## Run the tests

```powershell
python -m unittest discover -s tests -v
```

## Continuous Integration

Python unittest is used with CI for GitHub Actions to automatically run the complete test suite whenever changes are pushed or pulled.

## TDD approach

Each new behaviour was written as a failing test before the smallest passing implementation was added.
The code was then refactored while the complete test suite remained green.
