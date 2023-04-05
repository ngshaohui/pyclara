# Dictionaries

Dictionaries are unordered collections

We store objects within it as a key-value pair

We can retrieve the value that has been stored by

```python
foobar = {"foo": 9, "bar": 42}
print(foobar["foo"])  # 9
print(foobar["bar"])  # 42
```

## Adding new items to the dictionary

We can add new items to a dictionary by specifying the key and assigning it the desired value.

```python
foobar = {}
foobar["foo"] = 9
foobar["bar"] = 42
print(foobar)  # {"foo": 9, "bar": 42}
```

## Updating items in a dictionary

Dictionaries have a characteristic where only unique keys are allowed to exist.

When the key specified has already been used before, it will overwrite the existing value instead of adding a duplicate one.

```python
foobar = {}
foobar["foo"] = 9  # non-existent key, key-value pair is added
print(foobar)  # {"foo": 9}
foobar["bar"] = 9  # non-existent key, key-value pair is added
print(foobar)  # {"foo": 9, "bar": 9}
foobar["foo"] = 42  # key already exists, value is updated
print(foobar)  # {"foo": 42, "bar": 9}
```

## Removing items from the dictionary

```python
foobar = {"foo": 9, "bar": 42}
del foobar["foo"]
print(foobar)  # {"bar": 42}
```

Do note that the `del` keyword can be used to remove a variable from the current scope if it is called on the variable name itself `del foobar`.

Unlike the keys, values can be repeated.

## Valid dictionary keys

Only immutable types can be used as dictionary keys

We will go through mutability and immutability in depth next time, but for now these are some immutable types we've encountered

- strings
- integers
- booleans (avoid this)

```python
foobar = {}
foobar["foo"] = "bar"  # string as key
foobar[0] = "baz"  # integer as key
print(foobar)  # {'foo': 'bar', 0: 'baz'}
```

A mutable type we've covered is `list`, so this cannot be used as a key reliably since its contents can change (mutable).

```python
foobar = {}
ls = [1]
foobar[ls] = 42
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: unhashable type: 'list
```

Likewise, a dictionary is an immutable type so it is not a valid dictionary key.

If we need to use immutable types like lists and dictionaries as a dictionary key for some reason, we can opt to stringify them first.

```python
ls = [1]
foobar[str(ls)] = 42
print(foobar)  # {'bar': 42, '[1]': 42}
```

### Avoiding booleans

```python
foobar = {}
foobar[True] = "foo"
print(foobar)  # {True: 'foo'}
foobar[1] = "bar"
print(foobar)  # {True: 'bar'}
foobar[2] = "baz"
print(foobar)  # {True: 'bar', 2: 'baz'}
```

Since the integer 1 also evaluates to `True`, this leads to confusing behaviour as a pre-existing key value of `True` will be overwritten when 1 is subsequently used as a key.

## Possible dictionary values

Unlike keys, we can use both mutable and immutable types for our keys.

```python
foobar = {"name": "bob"}
foobar["tags"] = ["tall", "dark", "handsome"]
print(foobar)  # {'name': 'bob', 'tags': ['tall', 'dark', 'handsome']}
```

If the value is a mutable object, we may change it without reassigning

```python
foobar = {"name": "bob", "tags": ["tall", "dark", "handsome"]}
foobar["name"] = "bobby"  # need to use reassignment to update immutable values
foobar["tags"].append("agile")
print(foobar["tags"])  # ['tall', 'dark', 'handsome', 'agile']
```

We may still use reassignment (`=` operator) to update its value, but take note that this creates a brand new object. We will gain a deeper understanding into objects and references next time.

## Check existence of key in dictionary

A common use case for dictionaries is to keep track of items encountered.

We may check for the existence of a key in a dictionary with the `in` operator.

```python
foobar = {"foo": 9, "bar": 42}
print("foo" in foobar)  # True
print("bar" in foobar)  # True
print("foobar" in foobar)  # False
```

However, take note that we can not check for the existence of values within a dictionary.

One way to circumvent this can be to create a second dictionary with the values as the keys.

## Dictionary iterators

### Get all pairs

```python
foobar = {"foo": 9, "bar": 42}
for k, v in foobar.items():
    print("key:", k, "value:" v)
```

### Get only keys

```python
foobar = {"foo": 9, "bar": 42}
foobar_keys = foobar.keys()
print(foobar_keys)  # dict_keys(['foo', 'bar'])
```

### Get only values

```python
foobar = {"foo": 9, "bar": 42}
foobar_values = foobar.values()
print(foobar_values)  # dict_values([9, 42])
```

## Examples

### Counting frequency of element in a list

Count the number of times each element appears in the list

```python
ls = [1, 2, 3, 4, 1, 2, 4, 1, 2, 6, 4, 2, 1, 4, 3, 9, 1, 6, 4]
freq: dict[int, int] = {}
for num in ls:
    if num in freq:
        # increment frequency of encounter
        freq[num] += 1
    else:
        # element has not been seen before
        freq[num] = 1  # set frequency of encounter as 1
for k, v in freq.items():
    print(f"element {k} has been seen {v} time(s)")
```

### Simple phone book

Phone book example

```python
phone_book = {}
print("get [name]")
print("add [name] [number]")
while True:
    user_input = input("Query: ")
    tokens = user_input.split(" ")
    if tokens[0] == "get":
        if tokens[1] in phone_book:
            print(phone_book[tokens[1]])
        else:
            print(f"{tokens[1]} not in phone book")
    elif tokens[0] == "add":
        phone_book[tokens[1]] = tokens[2]
        print(f"added {tokens[1]} with phone number {tokens[2]}")
    else:
        print("unknown command")
```
