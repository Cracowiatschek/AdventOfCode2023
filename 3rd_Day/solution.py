# part one | *
import re


file = open('input.in', 'r').read()
example = open('example.in', 'r').read()

punctuation = set(list(re.findall("[^A-Za-z0-9]", file)))
punctuation.remove('.')
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

file = file.split('\n')
example = example.split('\n')


def search_engine_schema(filepath):
    engine_schema = []
    column = 0
    for line in filepath:
        punctuation_index = [[column, index] for index, char in enumerate(list(line)) if char in punctuation]

        if len(punctuation_index) != 0:
            for index in punctuation_index:
                numbers_area = [
                    [index[0] - 1, index[1] - 1], [index[0] - 1, index[1]], [index[0] - 1, index[1] + 1],
                    [index[0], index[1] - 1], [index[0], index[1] + 1],
                    [index[0] + 1, index[1] - 1], [index[0]+1, index[1]], [index[0] - 1, index[1] + 1]
                ]
                for area in numbers_area:
                    engine_schema.append([area, index])

        column += 1

    return engine_schema


def engine_mapper(filepath):
    column = 0
    number_positions = []
    for line in filepath:
        digits_index = [[val, column, index] for index, val in enumerate(list(line)) if val in digits]
        text_numbers = re.findall(r'\d+', line)

        container = []
        temp_index = []
        for digit in digits_index:
            container.append(digit[0])
            temp_index.append(digit[1:])

            concat_container = ''.join(container)
            if concat_container in text_numbers:
                for index in temp_index:
                    number_positions.append([concat_container, index[0], index[1]])
                container.clear()
                temp_index.clear()
        column += 1
    return number_positions


def engine_calculations(engine_part_positions, engine_schema):
    solution = []
    unique_parts = []
    for parts in engine_part_positions:
        for schema in engine_schema:
            if parts[1:] == schema[0]:
                solution.append([parts[0], schema[1]])

    for solution_parts in solution:
        if solution_parts not in unique_parts:
            unique_parts.append(solution_parts)

    solution_score = []

    for parts in unique_parts:
        solution_score.append(int(parts[0]))

    return sum(solution_score)


def solve_part_one(filepath):
    engine_schema = search_engine_schema(filepath)
    engine_part_positions = engine_mapper(filepath)
    solution = engine_calculations(engine_schema=engine_schema,engine_part_positions=engine_part_positions)
    return solution


print(solve_part_one(file))
