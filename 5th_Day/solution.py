# part one | *

example = open('example.in', 'r').read().split('\n')
file = open('input.in', 'r').read().split('\n')


def gardener_map(filepath):
    garden_map = {
        'seeds': [],
        'seed-to-soil': [],
        'soil-to-fertilizer': [],
        'fertilizer-to-water': [],
        'water-to-light': [],
        'light-to-temperature': [],
        'temperature-to-humidity': [],
        'humidity-to-location': []
    }
    label = ''
    for i in filepath:
        line = i.split(' ')

        if len(line[0]) != 0:
            check_tag = list(line[0])[-1]
            if check_tag == ':':
                if line[0][:-1] in garden_map:
                    label = line[0][:-1]
            elif line[0].isdigit():
                label = label
            else:
                if line[0] in garden_map:
                    label = line[0]

        params = []
        for n in line:
            if n.isdigit() and label == 'seeds':
                garden_map[label].append(int(n))
            elif n.isdigit() and label != 'seeds':
                params.append(int(n))
                if len(params) == len(line):
                    garden_map[label].append(params)
                    params = []

    position = []
    for maps in garden_map:
        locate = []
        for item in garden_map[maps]:

            if maps == 'seeds':
                position.append(item)
            else:
                cache = position.copy()
                for n in cache:
                    if item[1] <= n <= item[1]+item[2]:
                        x = item[0] - item[1]
                        locate.append(n+x)
                        position.remove(n)

        for i in locate:
            position.append(i)
    return min(position)


solution = gardener_map(example)

print(f"\033[33m|------------------------------------------------------------|\033[0m")
print(f"\033[33m|\033[0mThe lowest location number from part one equal: \033[32m{solution}\033[33m          |")
print(f"\033[33m|------------------------------------------------------------|\033[0m")
# part two | **


def gardener_extended_map(filepath):
    garden_map = {
        'seeds': [],
        'seed-to-soil': [],
        'soil-to-fertilizer': [],
        'fertilizer-to-water': [],
        'water-to-light': [],
        'light-to-temperature': [],
        'temperature-to-humidity': [],
        'humidity-to-location': []
    }
    label = ''
    for i in filepath:
        line = i.split(' ')

        if len(line[0]) != 0:
            check_tag = list(line[0])[-1]
            if check_tag == ':':
                if line[0][:-1] in garden_map:
                    label = line[0][:-1]
            elif line[0].isdigit():
                label = label
            else:
                if line[0] in garden_map:
                    label = line[0]

        params = []
        for n in line:
            if n.isdigit() and label == 'seeds':
                garden_map[label].append(int(n))
            elif n.isdigit() and label != 'seeds':
                params.append(int(n))
                if len(params) == len(line):
                    garden_map[label].append(params)
                    params = []

    seeds_dict = garden_map['seeds']

    seed_extended = []
    for x in range(0, len(seeds_dict), 2):
        seed_extended.append([seeds_dict[x], seeds_dict[x]+seeds_dict[x+1]])

    del garden_map['seeds']

    ranges = seed_extended.copy()

    for maps in garden_map:

        locate = []

        while len(ranges) > 0:
            min_rng, max_rng = ranges.pop()

            for target, seed, rng in garden_map[maps]:
                minimal_common_point = max(min_rng, seed)
                maximum_common_point = min(max_rng, seed + rng)
                delta = target - seed
                if minimal_common_point < maximum_common_point:
                    locate.append([minimal_common_point + delta, maximum_common_point + delta])
                    if minimal_common_point > min_rng:
                        ranges.append([min_rng, minimal_common_point])
                    if max_rng > maximum_common_point:
                        ranges.append([maximum_common_point, max_rng])
                    break
            else:
                locate.append([min_rng, max_rng])
        solve = min(locate)[0]
        ranges = locate
    return solve


solution = gardener_extended_map(file)
print(f"\033[33m|\033[0mThe lowest location number from part two equal: \033[32m{solution}\033[33m    |")
print(f"\033[33m|------------------------------------------------------------|\033[0m")

