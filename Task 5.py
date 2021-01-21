def numbercalc():
    breaker = 0
    baselinesum = 0
    while breaker != 1:
        baseline = input("Введите строку чисел, разделенных пробелом:")
        datalist = baseline.split(" ")
        datalist.sort()
        if datalist[0] == "":
            datalist.remove("")
        print("Ваша строка: ",datalist)
        for i in datalist:
            try:
                int(i) / 1
            except ValueError:
                breaker = 1
                break
            else:
                baselinesum = int(i) + baselinesum

        print("Накопленная сумма: ", baselinesum)
    print("Операция закончена")


numbercalc()
