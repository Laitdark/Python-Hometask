firstarr = []
secondarr = []
stopper = ''
el = 0

while stopper != 'stop':
    userinput = input('Введите число (Для остановки - stop): ')
    if userinput == 'stop':
        stopper = 'stop'
    else:
        firstarr.append(int(userinput))

for i in firstarr:
    if i % 2 == 0:
        secondarr.append(el)
    el = el + 1

print('Первый массив:', firstarr, 'Второй массив:', secondarr)
