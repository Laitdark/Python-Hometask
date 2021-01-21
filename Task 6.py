def lowertoupper(lowerline):
    lowerline = lowerline[:1].swapcase() + lowerline[1:]
    return lowerline


baseline = input("Введите слово из латинских букв: ")
baseline = baseline.lower()
baseline = lowertoupper(baseline)
print(baseline)
longline = input("Введите более длинную строку: ")
longline = longline.lower()
longlinelist = longline.split()
longline = ""
for i in longlinelist:
    i = lowertoupper(i)
    longline = longline + i + " "
print(longline)
