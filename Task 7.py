userarray = []
stopper = ''
minelem = []

while stopper != 'stop':
    userinput = input('Введите число (Для остановки - stop): ')
    if userinput == 'stop':
        stopper = 'stop'
    else:
        userarray.append(int(userinput))

# Логика minelem - 0 элемент наименьший, 1 элемент второй по меньшинству. может быть равен 0-му
if userarray[0] < userarray[1]:
    minelem.append(userarray[0])
    minelem.append(userarray[1])
else:
    minelem.append(userarray[1])
    minelem.append(userarray[0])

for i in userarray:
    if i < minelem[0]:
        minelem[1] = minelem[0]
        minelem[0] = i
    elif i < minelem[1]:
        minelem[1] = i

print('В массиве:', userarray, 'минимальные элементы:', minelem)
