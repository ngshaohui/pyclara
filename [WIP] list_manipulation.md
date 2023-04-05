# List manipulation

## Iterators

Iterators are an object which allows us to step through each element in a collection

We have to imagine having a cursor and then stepping through a list

```python
ls = [1, 2, 3, 4, 5]
ls_iter = iter(ls)

# [| 1, 2, 3, 4, 5]  # the | symbol indicates the position of the cursor
```

When we ask for the next element, the cursor will return the item next to the iterator, in this case the value 1

```python
# [1, | 2, 3, 4, 5]
```

After iterating, the cursor will be at the next element in the list

```python
# [1, 2, 3, 4, 5 |]
```

After returning the last element in the list, the cursor will be at the back of the list, and no items are to the right of it

Attempting to iterate on this iterable will indicate that there are no items left

If we want to iterate from the front again, we can 

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
