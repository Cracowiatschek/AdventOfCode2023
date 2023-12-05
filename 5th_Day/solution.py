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
    cache = []
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


solution = gardener_map(file)

print(solution)
