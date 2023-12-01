import re

# part one | *

file = open('input.in', 'r').read().split('\n')

def calibrator(calibration_data):
    digit = []
    for line in calibration_data:
        num = ''.join(filter(str.isdigit, line))
        num = int(num[0] + num[-1])
        digit.append(num)

    return digit


solution = sum(calibrator(file))

print(f"\033[33m|------------------------------------------------------------|\033[0m")
print(f"\033[33m|\033[0mSum of the all calibration values from part one equal: \033[32m{solution}\033[33m|")
print(f"\033[33m|------------------------------------------------------------|\033[0m")
# part two | **

words_num = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', '1', '2', '3', '4', '5',
             '6', '7', '8', '9']

num_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, '1': 1,
            '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def calibrator_str(calibration_data):
    digit = []
    for line in calibration_data:
        first_digit = re.search(r"(one|two|three|four|five|six|seven|eight|nine|[0-9])", line)[0]
        last_digit = re.search(r"(enin|thgie|neves|xis|evif|ruof|eerht|owt|eno|[0-9])", line[::-1])[0][::-1]
        first_digit = num_dict[first_digit]
        last_digit = num_dict[last_digit]
        digit.append(int(str(first_digit)+str(last_digit)))
    return digit


solution = sum(calibrator_str(file))
print(f"\033[33m|\033[0mSum of the all calibration values from part two equal: \033[32m{solution}\033[33m|")
print(f"\033[33m|------------------------------------------------------------|\033[0m")
