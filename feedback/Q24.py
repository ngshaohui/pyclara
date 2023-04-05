# Q24

# print out every multiple of 5 between the range 0 and 100 (inclusive)
# i.e. 5, 10, 15, ..., 95, 100

# SH: (Correctness - Logic error)
# the second parameter of the range function is exclusive, so 100 is not printed
# we need to increment the range to 101 to fulfil the requirements of the question
for x in range(0,100,5):
    print (x)