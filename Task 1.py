userline = "1"
fullline = []
while userline != "":
    userline = input("Введите строку. Для окончания оставьте пустым: ")
    fullline.append(userline)

with open('Task1.txt', 'tw', encoding='utf-8') as taskonefile:
    for i in fullline:
        taskonefile.write(i+"\n")
taskonefile.close()