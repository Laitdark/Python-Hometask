
switchinglist = []
abortinput = ""
while abortinput != "end":
    addition = int(input("Пожалуйста, введите число: "))
    switchinglist.append(addition)
    abortinput = input("Для окончания ввода введите end: ")

print("Ваш базовый список:", switchinglist)

firstelement = 0
secondelement = 1
listlength =len(switchinglist)

while secondelement < listlength:
    switcherone = switchinglist[secondelement]
    switchertwo = switchinglist[firstelement]
    switchinglist[firstelement]=switcherone
    switchinglist[secondelement]=switchertwo
    firstelement = firstelement + 2
    secondelement = secondelement + 2

print("Ваш новый список:", switchinglist)
