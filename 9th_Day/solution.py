# part one | *

example = open('example.in', 'r').read().split('\n')
file = open('input.in', 'r').read().split('\n')



def make_difference(source):

    i = 0
    result = []
    for n in range(len(source) - 1):
        a = source[i]
        b = source[i + 1]
        diff = b - a
        i += 1
        result.append(diff)
    return result


def oasis(filepath):
    solve = []
    for i in filepath:
        x = [int(n) for n in i.split(' ')]
        stack = {}
        stack[0] = x
        end = x
        n = 1
        while sum(end) != 0:
            max_key = max(stack.keys())
            x = make_difference(stack[max_key])
            stack[n] = x
            end = x
            n += 1

        calculation = []
        for x in stack:
            calculation.append(stack[x][-1])

        calculation.reverse()
        n = 1
        result = calculation[0]
        check = [calculation[0]]

        for i in range(len(calculation) - 1):
            result = result + calculation[n]
            check.append(result)
            n += 1
        solve.append(result)
        print(stack)
        print(check)
    print(solve)
    return sum(solve)


solution = oasis(file)
print(solution)
