def fact(n):
    k = [el for el in range(n + 1)]
    k.remove(0)
    for el in k:
        factorial = 1
        n = el
        while n > 1:
            factorial *= n
            n -= 1
        yield factorial


n = int(input("Введите число: "))
for el in fact(n):
    print(el)
