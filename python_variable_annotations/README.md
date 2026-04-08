# Python - Variable Annotations

## Description

This project introduces **type annotations** in Python 3. Type annotations allow developers to specify the expected types of function arguments, return values, and variables. While Python does not enforce these types at runtime, annotations improve code readability, enable static type checking with tools like `mypy`, and are widely used in professional Python development.

## Learning Objectives

At the end of this project, you should be able to explain:

- Type annotations in Python 3
- How to use type annotations to specify function signatures and variable types
- Duck typing
- How to validate your code with `mypy`

## Requirements

- Python 3.9 (Ubuntu 20.04 LTS)
- `pycodestyle` style (version 2.5)
- All files must be executable
- All files must end with a new line
- First line of all files: `#!/usr/bin/env python3`
- All modules, classes, and functions must have documentation (docstrings)

## Tasks

### 0. Basic annotations - add
**File:** `0-add.py`

A type-annotated function `add` that takes two floats `a` and `b` and returns their sum as a float.

```python
def add(a: float, b: float) -> float:
```

### 1. Basic annotations - concat
**File:** `1-concat.py`

A type-annotated function `concat` that takes two strings `str1` and `str2` and returns their concatenation.

```python
def concat(str1: str, str2: str) -> str:
```

### 2. Basic annotations - floor
**File:** `2-floor.py`

A type-annotated function `floor` that takes a float `n` and returns the floor of the float as an integer.

```python
def floor(n: float) -> int:
```

### 3. Basic annotations - to string
**File:** `3-to_str.py`

A type-annotated function `to_str` that takes a float `n` and returns its string representation.

```python
def to_str(n: float) -> str:
```

### 4. Define variables
**File:** `4-define_variables.py`

Defines and annotates the following variables:

```python
a: int = 1
pi: float = 3.14
i_understand_annotations: bool = True
school: str = "Holberton"
```

### 5. Complex types - list of floats
**File:** `5-sum_list.py`

A type-annotated function `sum_list` that takes a list of floats `input_list` and returns their sum as a float.

```python
def sum_list(input_list: List[float]) -> float:
```

### 6. Complex types - mixed list
**File:** `6-sum_mixed_list.py`

A type-annotated function `sum_mixed_list` that takes a list of integers and floats `mxd_lst` and returns their sum as a float.

```python
def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
```

### 7. Complex types - string and int/float to tuple
**File:** `7-to_kv.py`

A type-annotated function `to_kv` that takes a string `k` and an int or float `v` and returns a tuple. The first element is the string `k`, the second is the square of `v` annotated as a float.

```python
def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
```

### 8. Complex types - functions
**File:** `8-make_multiplier.py`

A type-annotated function `make_multiplier` that takes a float `multiplier` and returns a function that multiplies a float by `multiplier`.

```python
def make_multiplier(multiplier: float) -> Callable[[float], float]:
```

### 9. Let's duck type an iterable object
**File:** `9-element_length.py`

Annotates the parameters and return values of the function below:

```python
def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    return [(i, len(i)) for i in lst]
```

## Usage

```bash
# Run a specific task
python3 0-main.py

# Check types with mypy
mypy 0-add.py

# Check style with pycodestyle
pycodestyle 0-add.py
```

## Author

Holberton School - Python Variable Annotations project
