# part one | *
import re
import string

file = open('input.in', 'r').read().split('\n')

punctuation = list(string.punctuation)
punctuation.remove('.')
num = list(string.digits)

symbol_pos = []
engine_schema = []
number_pos = []
column = 0
for i in file:
    row_lst = list(i)
    index = [[column, index] for index, val in enumerate(row_lst) if val in punctuation]
    if len(index) != 0:
        for pos in index:
            engine_area = [
                [pos[0] + 1, pos[1] - 1], [pos[0] + 1, pos[1]], [pos[0] + 1, pos[1] + 1],
                [pos[0], pos[1] + 1], [pos[0], pos[1] - 1],
                [pos[0] - 1, pos[1] - 1], [pos[0] - 1, pos[1]], [pos[0] - 1, pos[1] + 1],
            ]
            symbol_pos.append(pos)
            for area in engine_area:
                engine_schema.append([area, [pos[0], pos[1]]])
    column += 1

column = 0
for i in file:
    row_lst = list(i)
    text_numbers = re.findall(r'\d+', i)
    numbers = [[val, column, index] for index, val in enumerate(row_lst) if val in num]

    container = []
    temp_index = []
    for n in numbers:
        container.append(n[0])
        temp_index.append(n[1:])
        var = ''.join(container)

        if var in text_numbers:
            for index in temp_index:
                number_pos.append([''.join(container), index[0], index[1]])

            container.clear()
            temp_index.clear()
    column += 1

engine_schema.sort()
pre_solution = []
for i in number_pos:
    for y in engine_schema:
        if i[1:] == y[0]:
            pre_solution.append([i[0], y[1]])

temp_solution = []
solution = []

for i in pre_solution:
    if i not in temp_solution:
        temp_solution.append(i)
        solution.append(int(i[0]))

print(sum(solution))