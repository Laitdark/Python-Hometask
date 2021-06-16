def checktheequation(n):
    i = 1
    equationleft = 0
    equationright = (n * (n + 1)) / 2
    while n > 0:
        equationleft = equationleft + i
        n = n - 1
        i = i + 1
    if equationleft != equationright:
        print('Error')
    else:
        print('  ', equationleft, '=', int(equationright), '\n Equation is true')


userline = ''
stopper = ''
while stopper != 'stop':
    userlength = input('Пожалуйста, введите длину ряда (Для остановки введите stop): ')
    if userlength == 'stop':
        stopper = 'stop'
        userline = userline + userlength
    else:
        userline = userline + userlength + ','

userline = userline.split(',')
userline.remove('stop')

for i in userline:
    print('Current length:', i)
    checktheequation(int(i))