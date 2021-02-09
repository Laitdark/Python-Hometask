class DivideByZeroDeleteUniverse(Exception):
    def __str__(self):
        return "Делить на ноль нельзя, иначе вселенная будет уничтожена"


def safedivision(numerator, denominator):
    if denominator == 0:
        raise DivideByZeroDeleteUniverse()
    else:
        return numerator / denominator

userinput=""
while userinput!="stop":
    numerator = int(input('Делимое: '))
    denominator = int(input('Делитель: '))

    try:
        print("Результат деления: ", safedivision(numerator, denominator))
    except DivideByZeroDeleteUniverse as e:
        print(e)
    userinput=input("Введите stop для прекращения: ")