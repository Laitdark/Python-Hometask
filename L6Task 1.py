import sys

def solutionone(userstart, userend):
    basearray = []
    divnine = 0
    divtwo = 0
    divtwoarr = []
    divninearr = []

    while userstart <= userend:
        basearray.append(userstart)
        userstart = userstart + 1

    for i in basearray:
        if i % 2 == 0:
            divtwo = divtwo + 1
            divtwoarr.append(i)
        if i % 9 == 0:
            divnine = divnine + 1
            divninearr.append(i)

    newarray = [divnine, divtwo, divninearr, divtwoarr]
    return newarray


def solutiontwo(userstart, userend):
    basearray = []
    divnine = 0
    divtwo = 0
    divtwoarr = []
    divninearr = []

    for i in range(userstart, userend + 1):
        if i % 2 == 0:
            divtwo = divtwo + 1
            divtwoarr.append(i)
        if i % 9 == 0:
            divnine = divnine + 1
            divninearr.append(i)

    newarray = [divnine, divtwo, divninearr, divtwoarr]
    return newarray


def solutionthree(userstart, userend):
    divnine = 0
    divtwo = 0

    for i in range(userstart, userend + 1):
        if i % 2 == 0:
            divtwo = divtwo + 1
        if i % 9 == 0:
            divnine = divnine + 1

    newarray = [divnine, divtwo]
    return newarray

def memory_count(lst):
    memory = 0

    for var in lst:
        spam = sys.getsizeof(var)

        if hasattr(var, '__iter__') and not isinstance(var, str):

            if hasattr(var, 'keys'):
                for key, value in var.items():
                    spam += memory_count([key]) + memory_count([value])

            else:
                spam += memory_count(var)

        memory += spam

    return memory

a=solutionone(2,99)
print('Sol1:',memory_count(a))
a=solutiontwo(2,99)
print('Sol2:',memory_count(a))
a=solutionthree(2,99)
print('Sol3:',memory_count(a))

# Взяты были три функции, прописанные еще для анализа 4 урока. Как мы можем видеть, фактически идентичную загрузку дают
# два варианта, выводящих массивы делителей. С учетом громоздкости первого по времени, он окончательно выпадает из вариантов решения
# Наибольшую компактность показать вариант номер 3, как и со временем. Но тут стоит вопрос наглядности. Если нужна наглядность - выбираем
# второй, если нет - берем третий
