userlength = int(input('Пожалуйста, введите длину ряда: '))
i = 1
theline = ''
linesum = 0

while userlength > 0:
    theline = theline + str(i) + ' '
    linesum = linesum + i
    i = i / -2
    userlength = userlength - 1

print('Sum of (', theline, ') is:', linesum)