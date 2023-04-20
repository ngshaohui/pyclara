# Lambdas

Lambdas are anonymous functions, ie functions that do not have a name.

## Anatomy of a lambda function

```python
def identity(x):
  return x

identity(42)  # 42
(lambda x: x)(42)  # 42

def addition(x: int, y: int) -> int:
  return x + y

addition(1, 5)  # 6
(lambda x, y: x + y) (1, 5)  # 6
```

A lambda function has 2 portions to it - the left and the right, which can be separated by the colon `:`.

Taking the identity function as our example, we can distinguish the left from the right:

Left: `lambda x`

Right: `x`

### Left

For everything from the `lambda` keyword right up to the colon `:`, this is the list of inputs.

### Right

For everything to the right of the colon `:`, this is the return value.

Note that we do not need an explicit `return` statement in a lambda function.

## Limitations

1. they're limited to only 1 line
2. limited ability to perform control flow (only able to utilise ternary operator)
3. not able to write test cases to test the lambda function you have written
4. errors thrown are not descriptive (will only be attributed to a lambda function)
5. unable to add type annotations

To expound on point 2

```python
lambda x: x if x > 2 else 0
```

This means that things like loops are not possible

## Reasons to use lambdas

Why would we want to use lambdas despite their limitations?

We might have some simple logic which we don't want to write as a function since it's too straightforward

For example, when destructuring a list of objects

```python
ls = [{'name': "bob", 'age': 10}, {'name': "billie", 'age': 12}]
xs = map(lambda x: x['name'], ls)
print(xs)  # gives us an iterable object
# we need to convert it to a list if we still want to work with lists later on
print(list(xs))  # [1, 4]
```

However depending on the complexity of the function, we might not want to use a lambda after all as we want to be able to test it

```python
user_obj = {
  "document": {
    "id": 123,
    "particulars": {
      "first_name": "billie",
      "last_name": "pratama"
    }
  }
}

def get_first_name(user_obj):
  return user_obj["document"]["particulars"]["first_name"]
```

by having a named function we are able to write a test for it

```python
def test_answer():
  assert get_first_name(user_obj) == "billie"
```

We can name lambda functions, but we might as well write a named function for it.

```python
subtraction = lambda x, y : x - y

def subtraction(x, y):
  return x - y
```

Lambdas give us the convenience to apply a quick operation in conjunction with map, filter, reduce

```python
# multiply each number by 3
ls = [1, 2, 3, 4, 5]
mul_ls = map(lambda x: x * 3, ls)

# get strings that contain e
ls = ["seeing", "is", "believing"]
e_ls = filter(lambda x: 'e' in x, ls)
```

## Summary

Lambda functions are essentially just named functions and can be used interchangeably.

There is no real situation where you can only use lambdas and not named functions, other than for the sake of convenience.
