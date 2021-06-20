# Усложняю на ввод начала и конца пользователем
userstart = int(input('Введите начальное число: '))
userend = int(input('Введите конечное число: '))
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

print('Кратные 2:', divtwo, 'Кратные 9:', divnine)
print('Список кратных 2:', divtwoarr)
print('Список кратных 9:', divninearr)
