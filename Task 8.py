#Это чуть доработанный мой класс с 7 урока основ Python. Про классы в условии ПЗ ничего не сказано, решил воспользоваться
class Matrix():
    def __init__(self, array):
        self.array = array

    def __str__(self):
        newstring = ''
        for i in self.array:
            tempstring = '| '
            for k in i:
                tempstring = tempstring + str(k) + ' '
            tempstring = tempstring + '|'
            newstring = newstring + tempstring + '\n'
        return newstring

    def __add__(self, other):
        return Matrix([[a[0] + a[1] for a in zip(b[0], b[1])] for b in zip(self.array, other.array)])


matheight = 1
matwidth = 1
tempmatrix = []
while matheight <= 4:
    temparray = []
    tempsum = 0
    while matwidth <= 4:
        userinput = int(input('Введите элемент ' + str(matheight) + ' строки: '))
        temparray.append(userinput)
        tempsum = tempsum + userinput
        matwidth = matwidth + 1
    temparray.append(tempsum)
    tempmatrix.append(temparray)
    matheight = matheight + 1
    matwidth = 1

classicmatrix = Matrix(tempmatrix)
print(classicmatrix)
