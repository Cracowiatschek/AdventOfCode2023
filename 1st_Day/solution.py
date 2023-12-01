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

print(f"Sum of the all calibration values is: \033[32m{solution}\033[0m")
print(f"\033[33m|------------------------------------------|\033[0m")
