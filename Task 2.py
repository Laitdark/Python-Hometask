usernumber = input('Пожалуйста, введите число: ')
even = 0
uneven = 0

for i in usernumber:
    if int(i) % 2 == 0:
        even = even + 1
    else:
        uneven = uneven + 1

print('Even:', even, 'Uneven:', uneven)