from collections import deque


def hexsum(x, y):
    HEX_NUM = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
               'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15,
               0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
               10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    result = deque()
    transfer = 0

    if len(x) > len(y):
        x, y = deque(y), deque(x)
    else:
        x, y = deque(x), deque(y)

    while x:

        if y:
            res = HEX_NUM[x.pop()] + HEX_NUM[y.pop()] + transfer

        else:
            res = HEX_NUM[x.pop()] + transfer

        transfer = 0

        if res < 16:
            result.appendleft(HEX_NUM[res])

        else:
            result.appendleft(HEX_NUM[res - 16])
            transfer = 1

    if transfer:
        result.appendleft('1')

    return list(result)


def hexmult(x, y):
    HEX_NUM = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
               'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15,
               0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
               10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    result = deque()
    spam = deque([deque() for _ in range(len(y))])

    x, y = x.copy(), deque(y)

    for i in range(len(y)):
        m = HEX_NUM[y.pop()]

        for j in range(len(x) - 1, -1, -1):
            spam[i].appendleft(m * HEX_NUM[x[j]])

        for _ in range(i):
            spam[i].append(0)

    transfer = 0

    for _ in range(len(spam[-1])):
        res = transfer

        for i in range(len(spam)):
            if spam[i]:
                res += spam[i].pop()

        if res < 16:
            result.appendleft(HEX_NUM[res])

        else:
            result.appendleft(HEX_NUM[res % 16])
            transfer = res // 16

    if transfer:
        result.appendleft(HEX_NUM[transfer])

    return list(result)


a = list(input('Введите 1-е шестнадцатиричное число: ').upper())
b = list(input('Введите 2-е шестнадцатиричное число: ').upper())
print(*a, '+', *b, '=', *hexsum(a, b))
print(*a, '*', *b, '=', *hexmult(a, b))
