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

The `sorted` function also 

## Sorting non-confirming lists

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
sorted(student_tuples, key=lambda student: student[2])  # sort by age
# [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
```

## How does sorting work?

As per usual, it helps to understand how we can accomplish sorting without standard library functions

Here are some straightforward sorting algorithms we can implement to sort our lists

### Bubble sort

This is the most straightforward sorting algorithm

### Selection sort

Maintains a sorted sublist within the list

### Insertion sort

## Efficiency of the 3 sorting methods discussed

### Merge sort


