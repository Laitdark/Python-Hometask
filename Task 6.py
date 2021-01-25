def lowertoupper(lowerline):
	lowerline=lowerline.lower()
	words=lowerline.split()
	lowerline=""
	for i in words:
		i = i[:1].swapcase() + i[1:]
		lowerline=lowerline+i+" "
	return lowerline
baseline = input("Введите текст из латинских букв: ")
baseline = lowertoupper(baseline)
print(baseline)
