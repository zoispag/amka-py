# amka-py

<a href="https://pypi.python.org/pypi/amka-py"><img alt="Pypi version" src="https://img.shields.io/pypi/v/amka-py.svg"></a>
![CI](https://github.com/zoispag/amka-py/workflows/CI/badge.svg)

A validator for greek social security number (AMKA)

## Installation

```bash
pip install amka-py
```
## Usage

```python
from amka_py.amka import validate

# An invalid AMKA
is_valid, err = validate("09095986680")
print(is_valid) # False
print(err)

# A valid AMKA
is_valid, err = validate("09095986684");
print(is_valid) # True
```
