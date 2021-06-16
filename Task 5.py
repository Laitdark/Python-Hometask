# Решил немного усложнить задачу и добавить возможность пользователя выбрать к-во пар, первый и последний символы.
# Работает корректно. Для полного соответствия условию можно взять параметры 10,32,127

def recursivetable(x, y, z):
    i = x
    line = ''
    while x > 0 and y <= z:
        line = line + str(y) + '- "' + chr(y) + '" ,'
        y = y + 1
        x = x - 1
    print(line)
    if y <= z:
        recursivetable(i, y, z)
    else:
        print('END')


linelength = int(input('Пожалуйста введите к-во пар в строке:'))
symone = int(input('Пожалуйста введите первый символ:'))
symtwo = int(input('Пожалуйста введите второй символ:'))

recursivetable(linelength, symone, symtwo)