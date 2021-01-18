

seasons = [[1, 2, 12], [3, 4, 5], [6, 7, 8], [9, 10, 11]]
seasonsdict = {"winter": [1, 2, 12], "spring": [3, 4, 5], "summer": [6, 7, 8], "autumn": [9, 10, 11]}
actualseason = ["winter", "spring", "summer", "autumn"]
iforlist = 0
listlength = len(seasons)
usermonth = int(input("Пожалуйста, введите номер месяца (1-12): "))

while iforlist < listlength:
    if usermonth in seasons[iforlist]:
        season = actualseason[iforlist]
        print("(Метод Списка) Ваш месяц входит в:", season)
    iforlist+=1

for keyseason, month in seasonsdict.items():
    if usermonth in month:
        print("(Метод Словаря) Ваш месяц входит в:", keyseason)

if usermonth <0 or usermonth >12:
    print ("Недопустимый месяц")