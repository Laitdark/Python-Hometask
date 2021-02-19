userstring = input("Введите строку, разделяя слова пробелами: ")
stringlist = userstring.split(" ")
number = 1
for i in stringlist:
    print(number, i[0:10])
    number += 1
