def reverse(line):
    reversedline = ''
    for i in line:
        reversedline = i + reversedline
    return reversedline


usernumber = input('Пожалуйста, введите число: ')
newnumber = reverse(usernumber)

print('Old number:', usernumber, 'New number:', newnumber)
