# SH: (remarks)
# good job!

# (Style - Formatting)
# remember to option+shift+f to run the autoformatter
# this will help to beautify your code, such as to remove trailing newlines

import re
# SH: (Design - Redundant code)
# the regex library is already imported above, no need to import search again
# likewise if using specific imports, no need to import the whole library again
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
horizontal_counter = 0
vertical_counter = 0
forward_counter = 0
up_counter = 0
down_counter = 0

while first_index <= len(command)-1:

    if search(forward_check, command[first_index]):
        # SH: (Formatting - Missing comments)
        # try to describe what the following does, as it is not that straightforward
        forward_counter= (int(re.search(r'\d+', command[first_index]).group()))
        horizontal_counter = (horizontal_counter + forward_counter)

    elif search(up_check, command[first_index]):
        up_counter = (-(int(re.search(r'\d+', command[first_index]).group())))
        vertical_counter = (vertical_counter + up_counter)
    
    else:
        down_counter = (int(re.search(r'\d+', command[first_index]).group()))
        vertical_counter = (vertical_counter + down_counter)

    first_index += 1

total = (horizontal_counter * vertical_counter)
print('total: ', total)


