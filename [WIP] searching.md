# Searching

One of the most common algorithms we use is to search for an element in a collection

Python has a lot of nice searching functions built in already for searching, which we can use instead of implementing our own

## Check if an element exists within a list

```python
ls = [1, 2, 3, 4, 5]
print(2 in ls)  # True
```

## Find the index of an item within a list

https://docs.python.org/3/tutorial/datastructures.html

```python
ls = [1, 2, 3, 4, 5]
print(ls.index(3))  # 2
```

That is nice and all, but how are these functions actually being performed?

## Linear search

The most straightforward way we can search is to examine every element in a collection

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

1. The intuition is to start in the middle of the list
2. If you have arrived at the element you are looking for, stop searching
   - If the element we are looking for is to the left of the list, discard the right of the list
   - If the element is to the right of the list, discard the left of the list
3. For the remaining list, repeat again from step 1

This allows us to search through the list in a much faster manner O(n) vs O(log n), where n is the size of the list

However, this is restricted to sorted lists only. For unsorted lists, we still need to examine every item in the list

## Built in binary search

Python has a built in function `bisect_left` which we may use to perform a binary search

https://docs.python.org/3/library/bisect.html#bisect.bisect_left

```python
def binary_search(ls: list[int], target: int) -> int:
  "Find index of target in ls, returns -1 if target does not exist in list"
  pos = bisect_left(ls, target)
  if != len(ls) and ls[pos] == target:
    return pos
  else:
    return -1

ls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# to search if 7 is in the list
print(linear_search(ls, 7))  # 6
```

## A quick understanding of time complexity

Time complexity is an important aspect of computer science, but we do not need to focus too much on it at this juncture
It is sufficient to be able to understand why some algorithms are more performant than others

A single operation will cost O(1)

```python
print("Hello world!")
```

Multiple operations will still only cost O(1)

```python
print("Hello")
print("world")
print("Goodbye")
print("world")
```

A loop will cost O(n) operations in the worst case

```python
ls = [1, 2, 3, 4, 5]
for i in ls:
  print(i)
```

consecutive loops will still cost O(n)
O(n) + O(n) = O(n)
```python
ls = [1, 2, 3, 4, 5]
for i in ls:
  print(i)
for i in ls:
  print(i)
```

nesting a loop within a loop will cost O(n^2)
O(n) * O(n) = O(n^2)
```python
ls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(len(ls)):
  for j in range(i + 1, len(ls)):
    print(i)
```
