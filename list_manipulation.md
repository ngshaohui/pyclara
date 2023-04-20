# List manipulation

Most of the data we work with in programming comes in the form of lists.

Python comes with a lot of useful built-in methods for processing lists.

## Combining lists

Combining lists is known as list concatenation.

### `+` operator

Lists can be combined using the `+` operator.

```python
xs = [1, 2, 3]
ys = [4, 5, 6]
ls = xs + ys
print(ls)  # [1, 2, 3, 4, 5, 6]
xs = [0]
print(ls)  # [1, 2, 3, 4, 5, 6]
```

We append the list `ys` to the back of `xs`, which creates a new list referenced by `ls`.

Since a new list is created, `ls` does not share any references with `xs` nor `ys` and any changes to the 2 lists will not affect `ls`.

### `extend` method

If we do not wish to create a new list, we can use the `extend` method to mutate the list.

```python
xs = [1, 2, 3]
ys = [4, 5, 6]
xs.extend(ys)
print(xs)  # [1, 2, 3, 4, 5, 6]
```

The method `extend` will append elements to the back of `xs`, and does not recreate the list.

This is synonymous to iterating through each element of the second list and appending it to the first.

```python
xs = [1, 2, 3]
ys = [4, 5, 6]
for element in ys:
  xs.append(element)
```

## Iterators

Iterators are objects which provide methods for us to step through each element in a collection.

This section serves as a primer on list manipulation functions that return iterators, such as `map` and `filter` in the next sections.

### Examples of iterables

All collections can be made into an iterable.

- list
- tuple
- dict

### Consuming an iterable

In order to work with the contents of an iterable, we will need to consume it by stepping through it.

It is synonymous to having a cursor and then stepping through a list.

```python
ls = [1, 2, 3, 4, 5]
ls_iter = iter(ls)

# [| 1, 2, 3, 4, 5]  # the | symbol indicates the position of the cursor
```

When we ask for the next element, the cursor will return the item next to the iterator, in this case the value 1:

```python
print(next(ls_iter))  # 1
# [1, | 2, 3, 4, 5]
```

We can call `next` again, and the cursor will be at the next element in the list.

```python
print(next(ls_iter))  # 2
# [1, 2, | 3, 4, 5]
```

We can continue iterating until we have reached the last element in the list, which can be visualised as follows:

```python
print(next(ls_iter))
# [1, 2, 3, 4, 5 |]
```

Once we are at the last element in the list, calling `next` again will throw an error since the iterable does not contain anymore elements.

```python
# [1, 2, 3, 4, 5 |]
print(next(ls_iter))
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# StopIteration
```

A full iteration cycle of the `iter` object is as follows:

```python
ls = [1, 2, 3, 4, 5]
ls_iter = iter(ls)
next(ls_iter)  # 1
next(ls_iter)  # 2
next(ls_iter)  # 3
next(ls_iter)  # 4
next(ls_iter)  # 5
next(ls_iter)  # Error as follows:
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# StopIteration
```

We can also opt to use `for .. in` to iterate through an `iter` object.

```python
ls_iter = iter([1, 2, 3])
for num in ls_iter:
  print(num)
# 1
# 2
# 3
```

### Differences with a `list`

Iterables can only be consumed once

```python
ls = [1, 2, 3, 4, 5]
print(list(ls))  # [1, 2, 3, 4, 5]
print(list(ls))  # [1, 2, 3, 4, 5]

ls_iter = iter([1, 2, 3, 4, 5])
print(list(ls_iter))  # [1, 2, 3, 4, 5]
print(list(ls_iter))  # []
```

If we need to use the contents more than once, we should save the contents to a list first.

```python
ls_iter = iter([1, 2, 3, 4, 5])
ls = list(ls_iter)
print(list(ls))  # [1, 2, 3, 4, 5]
print(list(ls))  # [1, 2, 3, 4, 5]
```

### Working with iterators

Iterators exist since they offer a clear predefined method to keep track of the current position in a collection.

They provide time and space efficiency in our code, since an operation can be deferred indefinitely until the element is requested (lazy evaluation). This also allows us to deal with other input sources of data such as streams, which could contain infinite elements.

As such, functions which commonly deal with list transformation by taking in a collection and outputting a collection would often choose to return an iterator.

However, the potential benefits for the aforementioned use case is commonly not experienced unless working with huge data sets.

It is acceptable to simply convert iterators to lists and work with them instead if that is more intuitive at this juncture while learning.

## Filter

The filter function takes in 2 arguments:

1. function that takes in an element and returns a `bool`
2. iterable

Only the elements that fulfil a predicate are kept in the final collection

```python
def is_even(num: int) -> bool:
  return num % 2 == 0

ls = [1, 2, 3, 4, 5]
filtered_ls = filter(is_even, ls)  # we expect to be left with [2, 4]
print(list(filtered_ls))  # [2, 4]
```

Without a filter function, it can be written as:

```python
def is_even(num: int) -> bool:
  return num % 2 == 0

ls = [1, 2, 3, 4, 5]
filtered_ls = []
# get list of even numbers from ls
for num in ls:
  if is_even(num):
    filtered_ls.append(num)
print(list(filtered_ls))  # [2, 4]
```

The main benefit of using a filter function is to evoke clarity in the expression.

Do note that there is no real performance gain between the two methods, so pick one that feels more comfortable.

A common application of this function is to filter a list of data by specific fields.

```python
def is_male(person) -> bool:
  return person["gender"] == "m"

people = [
  {"name": "bob", "gender": "m", "age": 42},
  {"name": "peter", "gender": "m", "age": 27},
  {"name": "alice", "gender": "f", "age": 77}
]
males = filter(is_male, people)
print(list(males))  # [{'name': 'bob', 'gender': 'm', 'age': 42}, {'name': 'peter', 'gender': 'm', 'age': 27}]
```

### Filter function does not return boolean

If the function passed to `filter` does not return a `bool`, the truthy value of the return value will be used.

```python
def no_return() -> None:
  return

ls = [1, 2, 3, 4, 5]
filtered_ls = filter(no_return, ls)
print(list(filtered_ls))  # []
```

By default, functions implicitly return `None` if no return value is specified.

Since the truthy value of `None` is `False`, this means that none of the elements can fulfil the predicate so the resulting list is empty.

Likewise, any non-boolean value will be converted into a boolean by assessing its truthy value, synonymous to returning `bool(value)`.

```python
def return_empty_str():
  return ''  # empty string evaluates to False

ls = [1, 2, 3, 4, 5]
filtered_ls = filter(return_empty_str, ls)
print(list(filtered_ls))  # []
```

Since `bool('')` evaluates to `False`, the filter function supplied can never be fulfiled.

```python
def return_foo_str():
  return 'foo'  # string with non-zero length evaluates to True

ls = [1, 2, 3, 4, 5]
filtered_ls = filter(return_foo_str, ls)
print(list(filtered_ls))  # [1, 2, 3, 4, 5]
```

Since `bool('foo')` evaluates to `True`, the filter function supplied will always be fulfiled.

As the outcome of these functions are determined without evaluating any inputs (arguments), we can say that these are vacuously `True` or `False`.

When encountering a completely empty or untouched list after applying a `filter`, it would be good to check if the supplied filter function has been correctly written.

## Map

The map function takes in 2 arguments:

1. function that takes in an element and returns another element
2. iterable

The map function takes a function, and applies it to every element within the iterable.

A common way to use this function is for data processing, where we want to transform a list

```python
def multiply_five(num: int) -> int:
  return num * 5

ls = [1, 2, 3, 4, 5]
mapped_ls = map(multiply_five, ls)
print(list(mapped_ls))  # [5, 10, 15, 20, 25]
```

```python
def to_upper(st: str) -> str:
  return st.upper()

# capitalise all words
words = ["foo", "BAR", "fooBAR"]
mapped_ls = map(to_upper, words)
print(list(mapped_ls))  # ['FOO', 'BAR', 'FOOBAR']
```

We can also map from one type to another:

```python
words = ["one", "two", "three"]
mapped_ls = map(len, words)
print(list(mapped_ls))  # [3, 3, 5]
```

Since the `len` function takes in a `str` and returns an `int`, we can map a list of strings to their corresponding lengths.

### No return statement

Remember that functions implicitly return `None` so if a function does not have a return statement.

```python
def no_return(arg) -> None:
  pass  # standalone return statement here will do the same thing

ls = [1, 2, 3, 4, 5]
mapped_ls = map(no_return, ls)
print(list(mapped_ls))  # [None, None, None, None, None]
```

Since `no_return` does not return any value explicitly, it returns `None` each time it is called, regardless of the argument supplied.

Each member of the list will be mapped to its corresponding return value, which is always `None`.
