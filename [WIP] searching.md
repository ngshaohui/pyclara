# Searching

One of the most common algorithms we frequently encounter is to search for an element in a collection.

Python has a lot of nice searching functions built in already for searching, which we can use instead of implementing our own.

https://docs.python.org/3/tutorial/datastructures.html#more-on-lists

## Check if an element exists within a list

We can use the `in` operator

```python
ls = [1, 2, 3, 4, 5]
print(2 in ls)  # True
```

## Find the index of an item within a list

```python
ls = [1, 2, 3, 4, 5]
print(ls.index(3))  # 2
```

In most cases, it suffices to use built-in methods, but there is benefit to understanding the intuition behind how they are achieved.

## Linear search

The most straightforward to can search is to examine every element in a collection.

```python
def linear_search(ls: list[int], target: int) -> int:
  "Find index of target in ls, returns -1 if target does not exist in list"
  for i in range(len(ls)):
    if ls[i] == target:
      return i
  return -1

ls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# to search if 7 is in the list
print(linear_search(ls, 7))  # 6
```

## Binary search

```python
ls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

One characteristic about this list is that it is in ascending order (the list is already sorted)

We may exploit this to do binary search

https://en.wikipedia.org/wiki/Binary_search_algorithm#Procedure

1. Examine the element in the middle of the list
2. If you have arrived at the element you are looking for, stop searching
   - If the element we are looking for is to the left half of the list, discard the right half of the list
   - If the element is to the right half of the list, discard the left half of the list
3. For the remaining list, repeat again from step 1

This allows us to search through the list in a much faster manner O(n) vs O(log n), where n is the size of the list.

However, this is restricted to sorted lists only. For unsorted lists, we still need to examine every item in the list.

## Built in binary search

Python has a built in function `bisect_left` which we may use to perform a binary search

https://docs.python.org/3/library/bisect.html#bisect.bisect_left
https://github.com/python/cpython/blob/dc08c7a51582027a412bdcf821a98b2af77b44c9/Lib/bisect.py#L68

```python
def binary_search(ls: list[int], target: int) -> int:
  "Find index of target in ls, returns -1 if target does not exist in list"
  pos = bisect_left(ls, target)
  if pos != len(ls) and ls[pos] == target:
    return pos
  else:
    return -1

ls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# to search if 7 is in the list
print(binary_search(ls, 7))  # 6
```

## A quick understanding of time complexity

Time complexity is an important aspect of computer science, but we do not need to focus too much on it at this juncture.

We only need to know enough to understand why some algorithms are more performant than others.

### Single operation

A single operation will cost O(1)

```python
print("Hello world!")  # O(1)
```

### Multiple consecutive operations

Multiple operations will still only cost O(1)

```python
print("Hello")  # O(1)
print("world")  # O(1)
print("Goodbye")  # O(1)
print("world")  # O(1)
```

### Single loop

A loop will cost O(n) operations in the worst case

```python
ls = [1, 2, 3, 4, 5]
for i in ls:  # O(n)
  print(i)  # O(1)
```

### Multiple consecutive loops

Consecutive loops will still cost O(n)
O(n) + O(n) = O(n)

```python
ls = [1, 2, 3, 4, 5]
for i in ls:  # O(n)
  print(i)
for i in ls:  # O(n)
  print(i)
```

### One nested loop

Nesting a loop within a loop will cost O(n^2)
O(n) * O(n) = O(n^2)

```python
ls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(len(ls)):  # O(n)
  for j in range(i + 1, len(ls)):  # O(n)
    print(i)
```
