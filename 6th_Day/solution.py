# part one | *

example = open('example.in', 'r').read().split('\n')
file = open('input.in', 'r').read().split('\n')


def get_record(filename):
    times = [int(t) for t in filename[0].split(' ') if t.isdigit()]
    records = [int(r) for r in filename[1].split(' ') if r.isdigit()]

    score = []
    n = 0
    for r in records:
        cnt = 0
        for i in range(times[n]+1):
            travel = i * 1 * (times[n] - i)
            if travel > r:
                cnt += 1
        score.append(cnt)
        n += 1

    solution = 1
    for x in score:
        solution *= x
    return solution


solution = get_record(file)
print(f"\033[33m|------------------------------------------------------------|\033[0m")
print(f"\033[33m|\033[0mMultiply of possibilities to win from part one equal: \033[32m{solution}\033[33m|")
print(f"\033[33m|------------------------------------------------------------|\033[0m")
# part two | **


def one_race(filename):
    times = int(''.join([t for t in filename[0].split(' ') if t.isdigit()]))
    record = int(''.join([t for t in filename[1].split(' ') if t.isdigit()]))

    score = 0
    for i in range(times + 1):
        travel = i * 1 * (times - i)
        if travel > record:
            score += 1
    return score


solution = one_race(file)
print(f"\033[33m|\033[0mPossibilities to win from part two equal: \033[32m{solution}\033[33m          |")
print(f"\033[33m|------------------------------------------------------------|\033[0m")
