class Matrix():
    def __init__(self, array):
        self.array = array

    def __str__(self):
        newstring = ""
        for i in self.array:
            tempstring = ""
            for k in i:
                tempstring = tempstring + str(k) + " "
            newstring = newstring + tempstring + "\n"
        return newstring

    def __add__(self, other):
        return Matrix([[a[0] + a[1] for a in zip(b[0], b[1])] for b in zip(self.array, other.array)])


matrixone = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrixtwo = Matrix([[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]])
print("Матрица 1:", matrixone, end="\n", sep="\n")
print("Матрица 2:", matrixtwo, end="\n", sep="\n")
print("Сумма Матриц:", matrixtwo + matrixone, sep="\n")
