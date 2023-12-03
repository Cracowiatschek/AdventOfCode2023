# part one | *

file = open('input.in', 'r').read().split('\n')
example = open('example.in', 'r').read().split('\n')


def engine_mapper(filepath):
    temp_solution = set()

    for row, content in enumerate(filepath):
        for index, char in enumerate(content):
            if char.isdigit() or char == '.':
                continue

            for y in [row - 1, row, row + 1]:
                for x in [index - 1, index, index + 1]:
                    if y < 0 or y >= len(filepath) or x < 0 or x >= len(filepath) or not filepath[y][x].isdigit():
                        continue
                    while x > 0 and filepath[y][x-1].isdigit():
                        x -= 1
                    temp_solution.add((y, x))

    solution = []
    for y, x in temp_solution:
        num = ""
        while x < len(filepath[y]) and filepath[y][x].isdigit():
            num += filepath[y][x]
            x += 1

        solution.append(int(num))
    return sum(solution)


solution = engine_mapper(file)
print(f"\033[33m|-------------------------------------------------------|\033[0m")
print(f"\033[33m|\033[0mSum of the all part numbers from part one equal: \033[32m{solution}\033[33m|")
print(f"\033[33m|-------------------------------------------------------|\033[0m")
# part two | **


def engine_gears(filepath):

    solution = []
    for row, content in enumerate(filepath):
        for index, char in enumerate(content):
            if char != '*':
                continue
            temp_solution = set()
            for y in [row - 1, row, row + 1]:
                for x in [index - 1, index, index + 1]:
                    if y < 0 or y >= len(filepath) or x < 0 or x >= len(filepath) or not filepath[y][x].isdigit():
                        continue
                    while x > 0 and filepath[y][x-1].isdigit():
                        x -= 1
                    temp_solution.add((y, x))

            if len(temp_solution) != 2:
                continue

            pre_solution = []
            for y, x in temp_solution:
                num = ""
                while x < len(filepath[y]) and filepath[y][x].isdigit():
                    num += filepath[y][x]
                    x += 1

                pre_solution.append(int(num))
            solution.append(pre_solution[0] * pre_solution[1])

    return sum(solution)


solution = engine_gears(file)
print(f"\033[33m|\033[0mSum of the all gear ratio from part two equal: \033[32m{solution}\033[33m|")
print(f"\033[33m|-------------------------------------------------------|\033[0m")
