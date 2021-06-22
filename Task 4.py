userarray = []
stopper = ''
maxcount = 0
maxelem = []

while stopper != 'stop':
    userinput = input('Введите число (Для остановки - stop): ')
    if userinput == 'stop':
        stopper = 'stop'
    else:
        userarray.append(int(userinput))

for i in userarray:
    if maxcount <= userarray.count(i):
        if maxcount == userarray.count(i):
            if maxelem.count(i) == 0:
                maxelem.append(i)
        else:
            maxelem = [i]
        maxcount = userarray.count(i)

print('Наибольшее к-во повторов:', maxcount, 'у элементов:', maxelem)
