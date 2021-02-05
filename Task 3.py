class Cell():
    def __init__(self, cellnumber):
        self.cellnumber = cellnumber

    def __str__(self):
        return "Cell(К-во клеток:{})".format(self.cellnumber)

    def __add__(self, other):
        return Cell(self.cellnumber + other.cellnumber)

    def __sub__(self, other):
        newcellnumber = self.cellnumber - other.cellnumber
        if newcellnumber > 0:
            return Cell(newcellnumber)
        else:
            raise ArithmeticError(newcellnumber)

    def __mul__(self, other):
        return Cell(self.cellnumber * other.cellnumber)

    def __truediv__(self, other):
        return Cell(self.cellnumber // other.cellnumber)

    def make_order(self, reqcellnumber):
        tempcellnumber = self.cellnumber
        reqcellnumberiteration = 1
        newstring = ''
        while tempcellnumber > 0:
            while reqcellnumberiteration <= reqcellnumber:
                newstring = newstring + "*"
                reqcellnumberiteration += 1
                tempcellnumber -= 1
            newstring = newstring + "\n"
            reqcellnumberiteration = 1
            if tempcellnumber < reqcellnumber:
                reqcellnumber = reqcellnumber - (reqcellnumber - tempcellnumber)
        return newstring


firstcell = Cell(52)
secondcell = Cell(40)
newcell = firstcell + secondcell

print("Результат сложения:", firstcell + secondcell)
try:
    print("Результат вычитания:", firstcell - secondcell)
except ArithmeticError:
    print("Результат вычитания: Ошибка, отрицательное значение")
print("Результат умножения:", firstcell * secondcell)
print("Результат деления:", firstcell / secondcell)
print(newcell.make_order(20))
