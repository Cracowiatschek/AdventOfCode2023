# part one | *

example = open('example.in').read().split('\n')
file = open('input.in').read().split('\n')


def card_mapper(card):
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
        cards = [card_mapper(card) for card in list(line.split(' ')[0])]
        value = int(line.split(' ')[1])
        hands_type = []
        for x in set(cards):
            cnt = cards.count(x)
            hands_type.append(cnt)
        hands_type.sort(reverse=True)
        hands_type = ''.join([str(x) for x in hands_type])
        score = figures[hands_type]
        if score == '11111':
            if cards[1] != cards[0] + 1 or cards[2] != cards[0] + 2 or cards[3] != cards[0] + 3 or cards[4] != cards[0] + 4:
                score = 0
            else:
                score = score
        else:
            score = score
        card_pocket[value] = cards
        score_pocket[score].append(value)
    print(score_pocket)

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


print(camel_cards(file))
