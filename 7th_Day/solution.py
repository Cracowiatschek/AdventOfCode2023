# part one | *

example = open('example.in').read().split('\n')
file = open('input.in').read().split('\n')


def card_mapper(card, mode):
    if mode == 'classic':
        card_map = {
                'A': 50,
                'K': 40,
                'Q': 30,
                'J': 20,
                'T': 10,
                '9': 9,
                '8': 8,
                '7': 7,
                '6': 6,
                '5': 5,
                '4': 4,
                '3': 3,
                '2': 2
            }
        return card_map[card]
    elif mode == 'without_joker':
        card_map = {
            'A': 50,
            'K': 40,
            'Q': 30,
            'T': 10,
            '9': 9,
            '8': 8,
            '7': 7,
            '6': 6,
            '5': 5,
            '4': 4,
            '3': 3,
            '2': 2
        }
        return card_map[card]
    elif mode == 'joker_score':
        card_map = {
            'A': 50,
            'K': 40,
            'Q': 30,
            'T': 10,
            '9': 9,
            '8': 8,
            '7': 7,
            '6': 6,
            '5': 5,
            '4': 4,
            '3': 3,
            '2': 2,
            'J': 1,
        }
        return card_map[card]


def camel_cards(filepath):

    figures = {
        '5': 7,
        '41': 6,
        '32': 5,
        '311': 4,
        '221': 3,
        '2111': 2,
        '11111': 1
    }

    card_pocket = {}
    score_pocket = {
        7: [],
        6: [],
        5: [],
        4: [],
        3: [],
        2: [],
        1: []
    }

    for line in filepath:
        cards = [card_mapper(card, 'classic') for card in list(line.split(' ')[0])]
        value = int(line.split(' ')[1])
        hands_type = []
        for x in set(cards):
            cnt = cards.count(x)
            hands_type.append(cnt)
        hands_type.sort(reverse=True)
        hands_type = ''.join([str(x) for x in hands_type])
        score = figures[hands_type]
        card_pocket[value] = cards
        score_pocket[score].append(value)

    result_to_calculate = []

    for i in score_pocket:
        if len(score_pocket[i]) == 0:
            continue
        else:
            check_list = []
            check_list_dct = {}
            for x in score_pocket[i]:
                values = card_pocket[x]
                values_to_dct = ''.join([str(x) for x in values])
                check_list.append(values)
                check_list_dct[values_to_dct] = x

            check_list.sort(key=lambda x: tuple(x), reverse=True)

            for x in check_list:
                values = ''.join([str(n) for n in x])
                result_to_calculate.append(check_list_dct[values])

    result_to_calculate.reverse()
    n = 1
    result = 0
    for x in result_to_calculate:
        result += x * n
        n += 1
    return result


solution = camel_cards(file)
print(f"\033[33m|--------------------------------------------------------|\033[0m")
print(f"\033[33m|\033[0mSum of the total winnings from part one equal: \033[32m{solution}\033[33m|")
print(f"\033[33m|--------------------------------------------------------|\033[0m")
# part two | **


def camel_cards_extended(filepath):

    figures = {
        '5': 8,
        '41': 7,
        '32': 6,
        '311': 5,
        '221': 4,
        '211': 3,
        '2111': 2,
        '11111': 1
    }

    card_pocket = {}
    score_pocket = {
        8: [],
        7: [],
        6: [],
        5: [],
        4: [],
        3: [],
        2: [],
        1: []
    }

    for line in filepath:
        trim_set = [card_mapper(card, 'without_joker') for card in list(line.split(' ')[0]) if card != 'J']
        if len(trim_set) == 0:
            trim_set = [50, 50, 50, 50, 50]
        check = []
        for x in set(trim_set):
            cnt = trim_set.count(x)
            check.append(cnt)
        check.sort(reverse=True)
        if sum(check) != 5:
            check[0] = check[0] + 5 - sum(check)
        hands_type = ''.join([str(n) for n in check])

        cards = [card_mapper(card, 'joker_score') for card in list(line.split(' ')[0])]
        value = int(line.split(' ')[1])

        score = figures[hands_type]
        card_pocket[value] = cards
        score_pocket[score].append(value)

    result_to_calculate = []

    for i in score_pocket:
        if len(score_pocket[i]) == 0:
            continue
        else:
            check_list = []
            check_list_dct = {}
            for x in score_pocket[i]:
                values = card_pocket[x]
                values_to_dct = ''.join([str(x) for x in values])
                check_list.append(values)
                check_list_dct[values_to_dct] = x

            check_list.sort(key=lambda x: tuple(x), reverse=True)
            for x in check_list:
                values = ''.join([str(n) for n in x])
                result_to_calculate.append(check_list_dct[values])

    result_to_calculate.reverse()
    n = 1
    result = 0
    for x in result_to_calculate:
        result += x * n
        n += 1
    return result


solution = camel_cards_extended(file)

print(f"\033[33m|\033[0mSum of the total winnings from part one equal: \033[32m{solution}\033[33m|")
print(f"\033[33m|--------------------------------------------------------|\033[0m")

