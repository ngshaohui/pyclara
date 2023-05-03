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

A lambda function has 2 portions to it - the **left** and the **right**, which can be separated by the colon `:`.

Taking the identity function as our example, we can distinguish the left from the right:

Left: `lambda x`

Right: `x`

### Left

For everything on the left, from the `lambda` keyword right up to the colon `:`, this is the list of inputs.

### Right

For everything to the right of the colon `:`, this is the return value.

Note that we do not need an explicit `return` statement in a lambda function.

## Limitations

### Limited to only 1 line

https://docs.python.org/3/reference/expressions.html#lambda

Lambdas are limited to a single expression, so we can not have complex logic within them.

### Limited ability to perform control flow

There is no straightforward way to perform control flow with a single expression as control flows usually require more than one line.

```python
# if statement
if True:
  pass

# loop
while True:
  pass
```

There's a way to compress the `if` statement into a line, also known as the ternery operator:

```python
"foo" if x is "foobar" else "bar"
```

This is the only way we can accomplish control flow in a lambda function.

```python
lambda x: x if x > 2 else 0
```

However, things like loops are not possible.

### Not able to write test cases to test lambda functions

Tests are written in external files, calling the functions we want to test for each test case we have designed.

However, lambda functions can not be exported without being named.

The only way to export and test a lambda function will be to name it first, disqualifying it as a lambda function.

### Unable to add type annotations

Type annotations are not possible when using lambdas according to the python specification.

```python
def is_even(num: int) -> bool:
  return num % 2 == 0

lambda num: num % 2 == 0
```

## Reasons to use lambdas

While lambdas have a lot of limitations and undesirable traits, there are still valid use cases for them.

We might have some simple logic which we don't want to write as a function since it's too straightforward.

For example, when destructuring a list of objects:

```python
people = [{'name': "bob", 'age': 27}, {'name': "alice", 'age': 42}]
names = map(lambda x: x['name'], people)
print(list(names))  # ['bob', 'alice']
```

Since the logic is trivial enough, we can opt to have it as a lambda function for ease of use.

However depending on the complexity of the function, we might not want to use a lambda after all as we want to be able to test it

```python
user_obj = {
  "document": {
    "id": 123,
    "particulars": {
      "first_name": "bob",
      "last_name": "dylan"
    }
  }
}

def get_first_name(user_obj):
  return user_obj["document"]["particulars"]["first_name"]
```

By having a named function we are able to write a test for it:

```python
def test_answer():
  assert get_first_name(user_obj) == "bob"
```

We can name lambda functions, but we might as well write a named function for it.

```python
subtraction = lambda x, y : x - y

def subtraction(x, y):
  return x - y
```

Lambdas give us the convenience to apply a quick operation in conjunction with map, filter, reduce.

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
