def maxtwobetweenthree(*args):
    maxone = args[0]
    maxtwo = args[1]
    if args[2] > maxone:
        maxone = args[2]
    elif args[2] > maxtwo:
        maxtwo = args[2]

    print("Сумма максимальных аргументов:", int(maxone) + int(maxtwo))


a = int(input("Введите число а: "))
b = int(input("Введите число b: "))
c = int(input("Введите число c: "))

maxtwobetweenthree(a, b, c)
