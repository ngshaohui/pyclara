# Imports and modules

https://docs.python.org/3/reference/import.html

Python programs are usually made up of many different files, separated by their responsibilities.

This can be in the form of other files we have written ourselves, or packages that have been written by others.

```python
import requests  # import everything in package downloaded from pip
import some/other/script  # import everything in local module
from math import pi  # import specific constant from library
from bs4 import BeautifulSoup  # import specific function from library
import module.with_a.sub_module  # import submodule
from .local_package import local_function  # import local relative package
import some_long_module_name as module_name  # import with alias
```

## Local imports

- python programs are structured in modules

### Co-located files

```python
# foo.py
import bar
print("Hello from foo.py")
bar.foobar()
```

```python
# bar.py
print("Hello from bar.py")

def foobar():
  print("foobar")
```

Output

```
Hello from bar.py
Hello from foo.py
foobar
```

When we run `foo.py`, we will see `Hello from bar.py` being printed before the one from `foo.py` runs.

Any statements that are present in the file will be executed when a file is being imported.

TODO link this to the below section on why should we encapsulate things in a `main` function

### Co-located modules

## Built-in imports



## Library imports

### `pip`

`pip` stands for Pip Installs Packages (a recursive definition).

Most development tools we use require us to work with other libraries in our code

This is usually accessible through some public repository

In python's case, there are a lot of libraries available so this makes it easy to work with

We can use pip to install these packages to use

## Encapsulating your code in a `main` function

When viewing python code, it is common to see things being wrapped in a `main` function.

At the bottom of the file, this `main` function is being called in an `if` statement.

[python documentation](https://docs.python.org/3/library/__main__.html)

```python
def main():
  print("Hello world")


if __name__ == "__main__":
  main()
```

TODO - explanation
Main function will be called when a script is being run directly

However imported files will not run the main function explicitly
