# part one | *

example = open('example.in', 'r').read().split('\n')
file = open('input.in', 'r').read().split('\n')


def count_camel_step(filepath):
    directions = list(filepath[0])

    left_choice = {}
    right_choice = {}

    for i in filepath[2:]:
        get_key = i.split(' = ')[0]
        left_side = i.split(' = ')[1][1:-1].split(', ')[0]
        right_side = i.split(' = ')[1][1:-1].split(', ')[1]
        left_choice[get_key] = left_side
        right_choice[get_key] = right_side

    n = 'AAA'
    i = 0
    score = 0
    while n != 'ZZZ':
        if i >= len(directions):
            i = 0
        direct = directions[i]
        if direct == 'L':
            n = left_choice[n]
        else:
            n = right_choice[n]
        score += 1
        i += 1
    return score


print(count_camel_step(file))


def count_ghost_step(filepath):
    directions = list(filepath[0])

    left_choice = {}
    right_choice = {}
    check_key = []
    calculate = []
    for i in filepath[2:]:
        get_key = i.split(' = ')[0]
        if get_key[-1] in ['A', 'Z']:
            check_key.append(get_key)
        left_side = i.split(' = ')[1][1:-1].split(', ')[0]
        right_side = i.split(' = ')[1][1:-1].split(', ')[1]
        left_choice[get_key] = left_side
        right_choice[get_key] = right_side
    n = 'AAA'
    i = 0
    x = 1
    while check_key != calculate:
        if i >= len(directions):
            i = 0
        direct = directions[i]

        if direct == 'L':
            n = left_choice[n]
        else:
            n = right_choice[n]
        left_side = left_choice[n]
        right_side = right_choice[n]
        left_choice[get_key] = left_side
        right_choice[get_key] = right_side
    check_key.sort()
    print(check_key)


print(count_ghost_step(file))
