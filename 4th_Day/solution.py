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
print(f"\033[33m|\033[0mTotal points from part one equal: \033[32m{solution}\033[33m                |")
print(f"\033[33m|-------------------------------------------------------|\033[0m")


def how_many_cards(filename):
    card_list = []
    clear_card_list = []
    for card in filename:
        card_list.append(int(card.split(':')[0].split(' ')[-1]))
        clear_card_list.append(int(card.split(':')[0].split(' ')[-1]))

    id = 1

    copy_paste = {}

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

        copy_paste[id] = len(match_numbers)
        id += 1

    id = 1
    for i in clear_card_list:
        to_copy = clear_card_list[id:id+copy_paste[id]]
        cnt = card_list.count(i)
        for n in range(cnt):
            for copies in to_copy:
                card_list.append(copies)

        id += 1
    return len(card_list)


solution = how_many_cards(file)
print(f"\033[33m|\033[0mTotal count of cards from part two equal: \033[32m{solution}\033[33m      |")
print(f"\033[33m|-------------------------------------------------------|\033[0m")
