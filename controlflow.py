# What do the following output

# Example

if True:
    print("foo")
else:
    print("bar")

# Output:
# foo

i = 0
while i < 10:
    print(i)
    i = i + 1

# Output:
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9

# Q1

if True and False or False and True:
    print("foo")
else:
    print("bar")

# Q2

foo = 1 * 2 + 3

if foo < 10:
    print("foo")
elif foo < 8:
    print("bar")
else:
    print("foobar")

# Q3

foo = 6

if foo < 10:
    print("foo")
if foo < 8:
    print("bar")
else:
    print("foobar")

# Q4

foo = 6

if foo > 10:
    print("foo")
elif foo > 4:
    print("bar")

# Q5

foo = 6

if foo:
    print("foo")
else:
    print("none")

# Q6

foo = 0

if foo:
    print("foo")
else:
    print("none")

# Q7

ls = []

if ls:
    print("foo")
else:
    print("none")

# Q8

ls = [False]

if ls:
    print("foo")
else:
    print("none")

# Q9

obj_map = {"foo": True}

if obj_map:
    print("foo")
else:
    print("none")

# Q10

for x in []:
    print(x)

# Q11

for i in range(10):
    print(i)

# Q12

for i in range(10, 0):
    print(i)

# Q13

for i in range(10, 0, -1):
    print(i)

# Q14

for i in range(0, 10, 5):
    print(i)

# Q15

for i in range(10):
    if i > 5:
        break
    print(i)

# Q16

for ch in range(ord("c"), ord("f") + 1):
    print(chr(ch))

# Q17

for i in range(4):
    for j in range(i, i + 2):
        print(j)

# Q18

i = 0
while i < 10:
    i = i + 1
    print(i)

# Q19

i = 0
while True:
    i += 1
    if i == 5:
        break
    elif i == 2:
        continue
    print(i)

# Q20

i = 0
while i > 0:
    print("foo")

# Q21

# i = 0
# while True:
#     print(i)

# Q22

# write a for loop that prints out even numbers between 1 and 11
# hint: we can check if a number is even by utilising the modulo operator
# hint: we can also use range to achieve this with the step parameter

# Q23

# write a for loop that prints out alphabets from "a" to "z"

# Q24

# print out every multiple of 5 between the range 0 and 100 (inclusive)
# i.e. 5, 10, 15, ..., 95, 100
