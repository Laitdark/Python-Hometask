# Усложняю на ввод начала и конца пользователем
userstart = int(input('Введите начальное число: '))
userend = int(input('Введите конечное число: '))
divnine = 0
divtwo = 0
divtwoarr = []
divninearr = []

for i in range(userstart,userend+1):
    if i % 2 == 0:
        divtwo = divtwo + 1
        divtwoarr.append(i)
    if i % 9 == 0:
        divnine = divnine + 1
        divninearr.append(i)

print('Кратные 2:', divtwo, 'Кратные 9:', divnine)
print('Список кратных 2:', divtwoarr)
print('Список кратных 9:', divninearr)
