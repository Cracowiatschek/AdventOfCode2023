# part one | *

example = open('example.in', 'r').read().split('\n')
file = open('input.in', 'r').read().split('\n')


def score_card(filename):
    score = []

    for card in filename:
        winning_numbers = []
        my_numbers = []

        for num in card.split('|')[0].split(' ')[2:]:
            if num.isdigit():
                winning_numbers.append(int(num))

        for num in card.split('|')[1].split(' '):
            if num.isdigit():
                my_numbers.append(int(num))

        match_numbers = list(set(my_numbers) & set(winning_numbers))

        points = 1
        cnt = 0

        if len(match_numbers) > 0:
            for num in match_numbers:
                cnt += 1
                if cnt >= 2:
                    points *= 2
            score.append(points)

    return sum(score)


solution = score_card(file)
print(f"\033[33m|-------------------------------------------------------|\033[0m")
print(f"\033[33m|\033[0mTotal points from part one equal: \033[32m{solution}\033[33m|")
print(f"\033[33m|-------------------------------------------------------|\033[0m")
