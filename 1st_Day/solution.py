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

print(calibrator(file))
solution = sum(calibrator(file))

print(f"Sum of the all calibration values is: \033[32m{solution}\033[0m")
print(f"\033[33m|------------------------------------------|\033[0m")
# part two | **

words_num = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', '1', '2', '3', '4', '5',
             '6', '7', '8', '9']

num_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, '1': 1,
            '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def calibrator_str(calibration_data):
    digit = []
    for line in calibration_data:
        pattern = re.compile('|'.join(re.escape(x) for x in words_num), flags=re.IGNORECASE)
        n = pattern.findall(line)
        x = []
        for i in n:
            x.append(num_dict[i])
        digit.append(int(str(x[0])+str(x[-1])))
    return digit


print(calibrator_str(file))
solution = sum(calibrator_str(file))
print(solution)

