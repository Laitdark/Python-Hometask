usernumber = input("Пожалуйста, введите трехзначное число: ")

if usernumber.isnumeric()==False:
    print("ERROR")
elif int(usernumber) < 100 or int(usernumber) > 999:
    print("ERROR")
else:
    c = int(usernumber) % 10
    b = (int(usernumber) // 10) % 10
    a = ((int(usernumber) // 10) // 10) % 10
    print(a, b, c)
    usersum = a + b + c
    usermult = a * b * c
    print("Sum", usersum, "Mult", usermult)
