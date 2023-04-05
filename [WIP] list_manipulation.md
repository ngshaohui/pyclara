# List manipulation

## Iterators

Iterators are objects which provide methods for us to step through each element in a collection.

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

## Filter

As the name implies, we want to filter out elements in a list

Only the elements that fulfil a predicate are kept

```python
def is_even(num: int) -> bool:
  return num % 2 == 0

ls = [1, 2, 3, 4, 5]
filtered_ls = filter(is_even, ls)  # we expect to be left with [2, 4]
print(list(filtered_ls))  # [2, 4]
```

## Map

We want to apply an operation over the entire list

```python
def multiply_five(num: int) -> int:
  return num * 5

ls = [1, 2, 3, 4, 5]
mapped_ls = map(multiply_five, ls)
print(list(mapped_ls))
