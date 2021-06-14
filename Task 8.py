useryear=int(input("Введите год: "))
divisionleftover=useryear%4

if divisionleftover==0:
    if useryear%100==0:
    	if useryear%400==0:
    		print(useryear, "Високосный")
    	else:
    		print(useryear, "Не високосный")
    else:
	    print(useryear, "Високосный")
else:
    print(useryear, "Не високосный")
