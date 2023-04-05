# Lambdas

list iterators

only need to teach identity functions after teaching map, filter, reduce
will also need to teach about the iterable object

```python

def identity(x):
  return x

identity(42)
(lambda x: x)(42)

def addition(x: int, y: int) -> int:
  return x + y

addition(1, 5)
(lambda x, y: x + y) (1, 5)
```

In short, this aims to demonstrate that lambda functions are essentially just named functions and can be used interchangeably

What are the applications of lambda functions?

There is no real situation where you can only use lambdas and not named functions

Do they take up less space when writing code?
Yes but not really
```python
lambda x: x

def f(x): return x
```

Other limitations

1. they're limited to only 1 line
2. limited ability to perform control flow (only able to utilise ternary operator)
3. not able to write test cases to test the lambda function you have written
4. errors thrown are not descriptive (will only be attributed to a lambda function)
5. unable to add type annotations

to expound on point 2

```python
lambda x: x if x > 2 else 0
```

This means that things like loops are not possible

So why would we ever want to use lambdas if they are so restrictive?
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

you can name lambda functions, but it is kinda useless

```python
subtraction = lambda x, y : x - y
```

ultimately, lambdas just give us the convenience to apply a quick operation in conjunction with map, filter, reduce

```python
# multiply each number by 3
ls = [1, 2, 3, 4, 5]
mul_ls = map(lambda x: x * 3, ls)

# get strings that contain e
ls = ["seeing", "is", "believing"]
e_ls = filter(lambda x: 'e' in x, ls)
```
