userletterone = input("Letter1: ")
userlettertwo = input("Letter2: ")
usernumber = int(input("Letter number:"))
positionone = ord(userletterone) - 96
positiontwo = ord(userlettertwo) - 96
distanceofletters = abs(positiontwo - positionone)-1
## Минус 1, так как в задании сказано к-во букв между ними, допустим между а и с будет одна буква, но без минуса оно посчитает некорректно (2)
numberletter = chr(usernumber + 96)

print("Letter1:", positionone, "Letter2:", positiontwo, "Inbetween:", distanceofletters)
print("Letter by number: ", numberletter)

## Чисто технически это можно все загнать в один единый принт после ввода, но я решил расписать все полностью с доп. переменными. Выглядит так:
print("\n\nLetter1:", ord(userletterone) - 96, "Letter2:", ord(userlettertwo) - 96, "Inbetween:", abs((ord(userletterone) - 96) - (ord(userlettertwo) - 96))-1, "Letter by number:", chr(usernumber + 96))