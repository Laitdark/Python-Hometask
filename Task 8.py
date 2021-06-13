useryear=int(input("Введите год: "))
divisionleftover=useryear%4

if divisionleftover==0:
    print(useryear, "Високосный")
else:
    print(useryear, "Не вискокосный")