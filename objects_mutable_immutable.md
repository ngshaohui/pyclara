# Mutable and Immutable objects

In python, everything is an object.

When we assign a value to a variable, an object is created with the value and a reference is stored in the variable.

```python
def foo():
    num = 42
```

The objects do not exist within the scope, only references do.

```python
def foo():
    num = 42
    bar()

def bar():
    num = 7
```

In the above example, the 2 scopes exist independently from each other and do not reference any same objects.

When an argument is passed to a child function, the child will reference the original object in the parent.

```python
def foo():
    num = 42
    bar(num)

def bar(arg):
    num = 7
```

In the above example, `arg` references the same `42` object as `num`.

However if we assign a new value to `arg`, it will no longer point to the same object as `num`.

```python
def foo():
    num = 42
    bar(num)

def bar(arg):
    arg = 20
    num = 7
```

`arg` starts out by referencing the same `42` as `num`.

The reassignment `arg = 20` causes it to reference a different object that contains `20`.

```python
def foo():
    num = 42
    num2 = bar()

def bar():
    num = 7
    return num
```

The `bar` function creates a variable `num` that refernces an object that contains `7`.

When we return `num`, the reference to the object is passed back to the parent scope.

Since the results of `bar` are being stored in `num2`, this effectively stores the reference being returned by the child scope.

## Mutable objects

Mutable objects are objects whose value can be changed (mutated).

This can be achieved when the object contains methods which allows us to update its value.

### Examples of mutable objects

- lists
- dictionaries

```python
def foo():
    ls = [42, 27]
    ls.append(7)
```

Just as with immutable variables, the list object itself does not exist within the scope, only the reference does.

When appending an element to the list, the object itself mutates, but the reference remains the same.

### Reassignment of mutable objects

As in the previous section, we can also use reassignment to make the variable contain a different value.

```python
def foo():
    ls = [42, 27]
    ls = [42, 27, 7]
```

In the above example, a new object of type `list` is created, and the variable `ls` is updated to store that object's reference.

Both methods lead to the same end result, though the former does it with 1 object and the latter with 2 objects.

There is no "correct" method to doing things, but it can be noted that creating more objects has a slight performance impact.

However, this is usually insignificant enough and whichever method you prefer can be used comfortably.

## Immutable objects

Conversely, objects whose value cannot be changed are referred to as immutable objects.

### Examples of immutable objects

- integers
- strings
- booleans
- tuples

```python
st = "foo"
st[0] = "b"  # attempt to replace 'f' with 'b'
# TypeError: 'str' object does not support item assignment

pair = ("foo", "bar")
pair[1] = "baz"  # attempt to replace "bar" with "baz"
# TypeError: 'tuple' object does not support item assignment
```

### Tuples

Lists and tuples are similar collections, except tuples are immutable.

We should use a tuple when we do not expect the data to change, and would otherwise use a list if we do not know in advance what the collection should contain.

This helps us prevent the unwanted modification of a collection.

### Strings vs Lists

Just like tuples, strings are an immutable collection of characters.

If we need to mutate a string, we have to create a new one.

This can be done by converting it to a list first, mutating the list, then converting back to a string.

```python
st = "foo"
ls = list(st)  # ['f', 'o', 'o']
ls[0] = "b" # ['b', 'o', 'o']
st = "".join(ls)  # 'boo'
```

## Copying object references

At this point, we have seen that reassignment can cause the references within the variable to change.

We have also seen how more than one variable can reference the same object when we pass function arguments.

```python
def foo():
    num = 42
    bar(num)

def bar(num_arg):
    return
```

In the above, `num_arg` in `bar` references the same object as `num` in `foo`.

We can also explicitly copy references when we assign one variable to another.

```python
def foo():
    num = 42
    num2 = num
```

By assigning one variable to another variable, we copy its reference. As such, both `num` and `num2` contain the same reference to `42`.

This can also be done for mutable objects as well, where `xs` and `ys` both contain the reference to the same list.

```python
def foo():
    xs = [42, 27]
    ys = xs
    print(xs)  # [42, 27]
    print(ys)  # [42, 27]
```

Since the object being referenced is mutable, calling mutation methods on either variable will result in the following.

```python
def foo():
    xs = [42, 27]
    ys = xs
    xs.append(7)
    print(xs)  # [42, 27, 7]
    print(ys)  # [42, 27, 7]
    ys.append(3)
    print(xs)  # [42, 27, 7, 3]
    print(ys)  # [42, 27, 7, 3]
```

Both variables contain the reference to the same object, so printing the values in `xs` and `ys` gives the same result.

If we want `xs` and `ys` to be separate lists, we should create a new list instead.

```python
def foo():
    xs = [42, 27]
    ys = xs
    xs = [7]
    print(xs)  # [7]
    print(ys)  # [42, 27]
```

If we need to copy the entire list, we can make use of the `list` function to clone the list.

```python
def foo():
    xs = [42, 27]
    ys = list(xs)
    xs.append(7)
    print(xs)  # [42, 27, 7]
    print(ys)  # [42, 27]
```

The `list` object creates a new `list` containing all the elements of the original list being passed as an argument.

An alternative way you might encounter this is to use the slice operator.

```python
def foo():
    xs = [42, 27]
    ys = xs[:]  # slice from start to end
    xs.append(7)
    print(xs)  # [42, 27, 7]
    print(ys)  # [42, 27]
```

When using the slice operator, this creates another `list` object with the elements specified in the range given.

Since passing an function arguments means passing an object's reference, we can mutate the object in a different function and the changes will persist.

```python
def foo():
    xs = [42, 27]
    bar(xs)
    print(xs)  # [42, 27, 7]

def bar(ls):
    ls.append(7)
```

When an argument is passed to a child function, the child will reference the original object in the parent.

Since the object being referenced is mutable, this allows the child scope to mutate a value which originates from its parent scope.

The takeaway here is that when passing mutable objects as arguments to another function, the objects can potentially be mutated.

This is in contrast with passing immutable objects, which will not affect the parent scope without a `return` statement.

## Notable differences between mutable and immutable objects

### Equality operators

We can use the `==` operator to check for value equality, but have to use the `is` operator to check for identity equality (if the 2 objects being compared refer to the same one)

#### Using `==` to check equality of objects

We often use the `==` operator to check if one value is equivalent to another value

```python
num % 2 == 0  # check if number is even
5 == 5
x != y
```

Likewise, we can use the `==` operator to check if the members of 2 lists are the same.

```python
xs = [1, 2, 3]
ys = [1, 2, 3]
xs == ys  # True
```

As lists are an ordered collection, it also requires that the elements be in the same position.

```python
xs = [1, 2, 3]
ys = [3, 2, 1]
xs == ys  # False
```

The `==` operator can also be used to check if 2 dictionaries are the same.

```python
d1 = {'foo': 1, 'bar': 2}
d2 = {'bar': 2, 'foo': 1}
d1 == d2  # True
```

As dictionaries are an unordered collection, it does not matter if the ordering is different as long as the contents are the same.

In general, the `==` operator can be used to check equality for Python's built-in collections:

- dict (unordered)
- list (ordered)
- set (unordered)
- tuple (ordered, immutable)

#### Using `is` to check equality of object reference

We can use the `is` operator to check if 2 variables reference the same object.

As we have seen previously, one instance where this occurs is when we copy an object's reference to another variable.

```python
xs = [1, 2, 3]
ys = xs
xs is ys  # True
```

`xs is ys` evaluates to `True` since they both point towards the same object in memory.

```python
xs = [1, 2, 3]
ys = [1, 2, 3]
xs is ys  # False
```

While objects might contain the same values, they contain different references if declared as separate objects.

```python
xs = [1, 2, 3]
ys = list(xs)
xs is ys  # False
```

When using a constructor to clone an object, it also creates a separate object.

### `id` function

Another way we can figure out which objects variables are referencing is by using the `id` function.

```python
def foo():
    num = 42
    print(id(num))
    bar(num)

def bar(arg):
    print(id(arg))
```

We expect the `num` and `arg` to reference the same objects, since `arg` is being passed as `num` from the parent scope `foo`.

Calling `foo()` gives the output below:

```
>>> foo()
4418855752
4418855752
```

Note that the object id being printed might be different across each run, but these 2 will always be the same within the run itself.

We can thus simulate the `is` operator by checking if the ids returned by `id` are the same.

```python
xs = [1, 2, 3]
ys = [1, 2, 3]
zs = xs
id(xs) == id(ys)  # False
id(xs) == id(zs)  # True

num1 = 42
num2 = num1
id(num1) == id(num2)  # True
```

#### Caution against using `is` to check for value equality

It is technically also possible use the `is` operator to check for value equality.

```python
foo = 42
bar = 42
print(id(foo) == id(bar))  # True
print(foo is bar)  # True
print(foo is 42)  # True, with warning
# SyntaxWarning: "is" with a literal. Did you mean "=="?
```

This is the observable behaviour in CPython but is [not guaranteed to work as per the language spec](https://docs.python.org/3.8/whatsnew/3.8.html#changes-in-python-behavior), so code written this way is at risk of indeterminate bahaviour depending on the python distribution being used.

Note that if you run the above code snippet using another variant of python, it is possible to print `False` instead.

CPython is the default python installation available when we install python from python.org.

> [CPython (the main implementation of Python) can reuse some objects to improve performance. For example, when it starts up, it pre-creates int objects for the numbers -5 to 256.](https://adamj.eu/tech/2020/01/21/why-does-python-3-8-syntaxwarning-for-is-literal/)

Thus, using `is` to check for value equality may return `False`:

```python
foo = 257  # use 257 since it falls outside of the range [-5, 256]
bar = 257
print(id(foo) == id(bar))  # False
print(foo is bar)  # False
print(foo is 257)  # False, with warning
# SyntaxWarning: "is" with a literal. Did you mean "=="?
```

Since `257` falls outside the range of `-5` to `256`, each time we assign a variable with this value, a new object has to be created.

This causes each reference equality check against `257` to fail.

However, we can still retain object equality when copying references.

```python
foo = 257
baz = foo
print(id(foo) == id(baz))  # True
```

All in all, remember to stick to `==` when comparing value equality.
