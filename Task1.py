def division(a, b):
    if b == 0:
        print("Делить на 0 нельзя")
    else:
        print("Результат деления а на b: ", a / b)


a = int(input("Пожалуйста, введите делимое число a: "))
b = int(input("Пожалуйста, введите делитель b: "))
division(a, b)
