# part one | *

file = open('input.in', 'r').read().split('\n')
game_dict = {
    'blue': 14,
    'green': 13,
    'red': 12
}


def game_passed(file):
    summary = []

    for i in file:
        game_id = int(i.split(' ')[1][:-1])
        games = i.split(';')
        sets = []
        for part in games:
            x = part.split(',')
            for n in x:
                data = n.split(' ')
                sets.append(data[-2:])
        wrong = []
        for part in sets:
            if part[1] in part and int(part[0]) > game_dict[part[1]]:
                wrong.append(part)
        if len(wrong) == 0:
            summary.append(game_id)

    return sum(summary)


solution = game_passed(file)
print(f"\033[33m|-------------------------------------------------|\033[0m")
print(f"\033[33m|\033[0mSum of the games id from part one equal: \033[32m{solution}\033[33m    |")
print(f"\033[33m|-------------------------------------------------|\033[0m")
# part two | **


def game_min_cubes(file):
    summary = []

    for i in file:
        games = i.split(';')
        sets = []
        cubes_dict = {
            'blue': [],
            'green': [],
            'red': []
        }
        for part in games:
            x = part.split(',')
            for n in x:
                data = n.split(' ')
                sets.append(data[-2:])
        for part in sets:
            cubes_dict[part[1]].append(int(part[0]))
        summary.append(max(cubes_dict['blue']) * max(cubes_dict['green']) * max(cubes_dict['red']))

    return sum(summary)


solution = game_min_cubes(file)
print(f"\033[33m|\033[0mSum of the games power from part two equal: \033[32m{solution}\033[33m|")
print(f"\033[33m|-------------------------------------------------|\033[0m")
