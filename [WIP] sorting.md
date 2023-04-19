# Sorting

## Utilising standard built-in methods

As with searching, most programming languages will have standard libraries to handle sorting so you do not have to implement your own

https://docs.python.org/3/howto/sorting.html

If we're working with a list, we can use the `.sort()` method to accomplish sorting

```python
ls = [5, 1, 2, 4, 3]
ls.sort()
print(ls)  # [1, 2, 3, 4, 5]
```

When using the `.sort()` method, this modifies the list in place, so the original list is mutated

If we want to preserve the ordering of the original list, we may use the `sorted` function

```python
ls = [5, 1, 2, 4, 3]
sorted_ls = sorted(ls)
print(sorted_ls)  # [1, 2, 3, 4, 5]
print(ls)  # [5, 1, 2, 4, 3]  - original list order does not change
```

## Sorting collection of objects

For a list of strings, they will be sorted according to lexicographpical order

```python
ls = ["hello", "this", "is", "patrick"]
print(sorted(ls))  # ['hello', 'is', 'patrick', 'this']
```

If the list contains objects, we can supply a `key` argument which takes a function which is called to make comparisons

```python
student_tuples = [
    ('john', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10),
]
sorted(student_tuples, key=lambda student: student[2])
# [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
```

## How does sorting work?

It helps to understand how we can accomplish sorting without standard library functions.

Here are some straightforward sorting algorithms we can implement to sort our lists.

### Bubble sort

1. Traverse down the list, comparing 2 elements at a time.

2. If the left is greater than the right, swap the left and right elements.

3. Repeat for the whole list until all the elements are in ascending order, ie no more swaps can be made.

### Selection sort

Maintains a sorted sublist on the left, and an unsorted sublist on the right.

1. Traverse down the list keeping track of the starting index of the unsorted list.

2. For each element in the unsorted sublist, keep reference of the minimum value and its index.

3. Swap the reference minimum value with the starting index of the unsorted list.

4. Increment index of unsorted list.

5. Repeat until no more unsorted elements remain on the right.

### Insertion sort

Maintains a sorted sublist on the left, and an unsorted sublist on the right.

1. Traverse down the list keeping track of the ending index of the sorted list.

2. For each element in the unsorted sublist, move it into its sorted position in the left sublist.

3. Repeat until no more unsorted elements remain on the right.

## A quick understanding of space complexity

Similar to time complexity, space is another metric we use to analyse algorithms.

However unlike time complexity, this tends to be a less valued metric since space is more readily available in modern systems.

Nonetheless, we should take care that our algorithms do not become too grossly inefficient.

### Single variable

```python
foo = 42
```

A single variable takes up constant space O(1)

### Multiple variables

```python
foo = 42
bar = 7
baz = 27
```

Multiple variables still takes up constant space O(1)

### Single list

### Nested list

N x N matrix

## Efficiency of the 3 sorting methods discussed

All 3 sorting methods have an O(n^2) time complexity, and O(1) space complexity

### Merge sort


