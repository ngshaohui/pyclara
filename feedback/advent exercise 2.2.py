import re
from re import search

with open("input.txt", "r") as f:
    # store each line of input.txt into a list
    lines = f.read().splitlines()
    command = []
    for line in lines:
        command.append(str(line))  # convert each string number into an string


forward_check = 'forward'
up_check = 'up'
first_index = 0
horizontal_position = 0
vertical_counter = 0
forward_counter = 0
up_counter = 0
down_counter = 0
depth = 0
aim = 0

while first_index <= len(command)-1:

    if search(forward_check, command[first_index]):
        forward_counter = (
            int(re.search(r'\d+', command[first_index]).group()))
        horizontal_position = (horizontal_position + forward_counter)
        depth = (forward_counter * aim) + depth

    elif search(up_check, command[first_index]):
        up_counter = (-(int(re.search(r'\d+', command[first_index]).group())))
        vertical_counter = (vertical_counter + up_counter)
        aim = (aim + up_counter)

    else:
        down_counter = (int(re.search(r'\d+', command[first_index]).group()))
        vertical_counter = (vertical_counter + down_counter)
        aim = (aim + down_counter)

    first_index += 1

total = (horizontal_position*depth)
print('total: ', total)
