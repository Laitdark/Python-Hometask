def exponentation(x, y):
    basex = x
    x = x ** y
    print("(Метод **) Ваш х в степени y составляет: ", x)
    i = -1
    x = basex
    while i > y:
        x = basex * x
        i = i - 1
    print("(Метод цикла) Ваш х в степени y составляет: ", 1 / x)


y = int(input("Введите отрицательную степень: "))
while y >= 0:
    y = int(input("Введите отрицательную степень: "))

x = int(input("Введите базовое число: "))

exponentation(x, y)
