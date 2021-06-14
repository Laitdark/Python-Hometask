a = int(input("Пожалуйста, введите первое число: "))
b = int(input("Пожалуйста, введите второе число: "))
c = int(input("Пожалуйста, введите третье число: "))

if ((a < b and a > c) or (a < c and a > b)):
    print("Первое посередине")
elif ((b < a and b > c) or (b < c and b > a)):
    print("Второе посередине")
elif ((c < b and c > a) or (c < a and c > b)):
    print("Третье посередине")
else:
    print("ERROR")
