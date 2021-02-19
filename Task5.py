baselist = [7, 5, 3, 3, 2]
print("Базовый список:", baselist)
userinput=""
while userinput!="end":
    usernumber = int(input("Введите новое число: "))
    baselist.append(usernumber)
    baselist.sort()
    baselist.reverse()
    print("Текущий список:",baselist)
    userinput=input("Для окончания введите end: ")

print("Итоговый список:",baselist)
