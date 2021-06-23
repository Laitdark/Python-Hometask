import timeit
import cProfile


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


userstart = int(input('Введите начальное число: '))
userend = int(input('Введите конечное число: '))

# Изначальная функция
print('Solution One')
basearray = solutionone(userstart, userend)
print('Кратные 2:', basearray[1], 'Кратные 9:', basearray[0])
print('Список кратных 2:', basearray[3])
print('Список кратных 9:', basearray[2])

cProfile.run('solutionone(userstart,userend)')
setup_code = 'solutionone(2,99)'
stmt_code = 'from main import solutionone'

# Перепишем с ренджем
print('Solution Two')
basearray = solutiontwo(userstart, userend)
print('Кратные 2:', basearray[1], 'Кратные 9:', basearray[0])
print('Список кратных 2:', basearray[3])
print('Список кратных 9:', basearray[2])

cProfile.run('solutiontwo(userstart,userend)')

# Избавимся от двух. доп.массивов
print('Solution Three')
basearray = solutionthree(userstart, userend)
print('Кратные 2:', basearray[1], 'Кратные 9:', basearray[0])

cProfile.run('solutionthree(userstart,userend)')

print('Solution One Time 1000:',timeit.timeit('solutionone(userstart,userend)',globals=globals(),number=1000))
print('Solution One Time 10000:',timeit.timeit('solutionone(userstart,userend)',globals=globals(),number=10000))

print('Solution Two Time 1000:',timeit.timeit('solutiontwo(userstart,userend)',globals=globals(),number=1000))
print('Solution Two Time 10000:',timeit.timeit('solutiontwo(userstart,userend)',globals=globals(),number=10000))

print('Solution Three Time 1000:',timeit.timeit('solutionthree(userstart,userend)',globals=globals(),number=1000))
print('Solution Three Time 10000:',timeit.timeit('solutionthree(userstart,userend)',globals=globals(),number=10000))

# Solution One Time 1000: 0.020647300000000257
# Solution One Time 10000: 0.24504579999999976
# Solution Two Time 1000: 0.011070600000000042
# Solution Two Time 10000: 0.14353660000000001
# Solution Three Time 1000: 0.011824100000000115
# Solution Three Time 10000: 0.09332800000000008
# Как видно из исхода с timeit, функцию лучше записать в виде диапазона, а не двух несвязных циклом, что отбрасывает
# вариант номер один как дельный сразу же (Экономия времени в два раза от варианта 2). Так же, в зависимости от целей
# наглядности, можно срезать время еще и не отображая массивы делителей, что даст еще где-то 15-25% экономии. По
# профилированию разница между тремя вариантами записи незначительна, уменьшается только к-во call'ов.
# Сложности: 1: O(2n) (2 цикла, рост в ~10 раз от к-ва элементов *10), 2,3: O(n) (1 цикл, так же рост где-то раз в 10)
#