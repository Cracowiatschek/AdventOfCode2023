import math
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


solution = count_camel_step(file)
print(f"\033[33m|------------------------------------------------------------------------------------------|\033[0m")
print(f"\033[33m|\033[0mSum of steps to 'ZZZ' from part one equal: \033[32m{solution}\033[33m                       "
      f"                   |")
print(f"\033[33m|------------------------------------------------------------------------------------------|\033[0m")
# part 2 | **


def count_ghost_step(filepath):
    directions = list(filepath[0])

    left_choice = {}
    right_choice = {}
    a_check_key = []
    z_check_key = []

    for i in filepath[2:]:
        get_key = i.split(' = ')[0]
        if get_key[-1] == 'A':
            a_check_key.append(get_key)
        left_side = i.split(' = ')[1][1:-1].split(', ')[0]
        right_side = i.split(' = ')[1][1:-1].split(', ')[1]
        left_choice[get_key] = left_side
        right_choice[get_key] = right_side

    scoring = []
    check = []
    for n in a_check_key:
        x = ''
        score = 0
        i = 0
        while x == '':
            if i >= len(directions):
                i = 0
            direct = directions[i]
            if direct == 'L':
                n = left_choice[n]
            else:
                n = right_choice[n]
            if n[-1] in ['Z']:
                x = n
                check.append(x)
            i += 1
            score += 1
        scoring.append(score)

    solve = scoring[0]

    for n in scoring[1:]:
        x = abs(solve * n) // math.gcd(solve, n)
        solve = x

    return solve


solution = count_ghost_step(file)
print(f"\033[33m|\033[0mSum of the total steps to all nodes thet eend with 'Z' from part two equal: "
      f"\033[32m{solution}\033[33m|")
print(f"\033[33m|------------------------------------------------------------------------------------------|\033[0m")
