with open('Task5.txt', 'tw', encoding='utf-8') as taskfivefile:
    userline = "1"
    fullline = []
    sum = 0
    while userline != "":
        userline = input("Введите число. Для окончания оставьте пустым: ")
        if userline != "":
            sum = int(userline) + sum
        taskfivefile.write(userline + " ")
    taskfivefile.write("\nСумма всех чисел: " + str(sum))
taskfivefile.close()
