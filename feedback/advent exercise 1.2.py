# SH: (remarks)
# good work solving this, logic is concise and straightforward, easy to understand

# (Feedback - Others)
# try to reuse variables since you have already declared them
# in the context of this question, we want to compare positions 1,2,3 with 2,3,4
# so perhaps we could simply declare
# second_index = first_index + 1
# third_index = second_index + 1
# fourth_index = third_index + 1
# this then allows us to immediately do our sums and comparisons
# first_total = numbers[first_index] + numbers[second_index] + numbers[third_index]
# second_total = numbers[second_index] + numbers[third_index] + numbers[fourth_index]

# alternatively, the logic for comparing positions is actually a bit straightforward so we may
# omit the use of variables to store the values if we so wish, and do the following instead
# first_total = numbers[first_index] + numbers[first_index + 1] + numbers[first_index + 2]
# second_total = numbers[first_index + 1] + numbers[first_index + 2] + numbers[first_index + 3]

with open("input.txt", "r") as f:
    # store each line of input.txt into a list
    lines = f.read().splitlines()
    # print(lines)  # ['199', '200', '208', '210', '200', '207', '240', '269', '260', '263']
    # take note that lines contains a list of strings
    numbers = []
    for line in lines:
        numbers.append(int(line))  # convert each string number into an integer
    # print(numbers)  # [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
    increment_count = 0
    decrement_count = 0
    first_index = 0


    while first_index <= len(numbers)-4:
        x = numbers[first_index]

        second_index = first_index+1
        y = numbers[second_index]

        third_index = second_index+1
        z = numbers[third_index]

        # print(third_index)
        # SH: (Design - Convoluted logic)
        # if you wish to, can also simplify it as
        # first_total = numbers[first_index] + numbers[second_index] + numbers[third_index]
        first_total = x + y + z

        # SH: (Design - Redundant code)
        # redundant line
        y = numbers[second_index]

        second_index = first_index+1
        y = numbers[second_index]

        third_index = second_index+1
        z = numbers[third_index]

        fourth_index = third_index+1
        a = numbers[fourth_index]

        # SH: (Design - Convoluted logic)
        # likewise this can also be simplified
        # second_total = numbers[second_index] + numbers[third_index] + numbers[fourth_index]
        second_total = y + z + a
        print("first total:", first_total)    
        print("second total:", second_total)

    
        if first_total < second_total:
            increment_count = increment_count+1

        else:
            decrement_count = decrement_count+1

        second_index += 1
        first_index += 1
        first_total = second_total           

    print('increment count:', increment_count,
          'decrement count:', decrement_count)

    # option + shift + f for auto indentation
