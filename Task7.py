class Complex(object):
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return Complex(self.real + other.real,
                       self.imag + other.imag)

    def __sub__(self, other):
        return Complex(self.real - other.real,
                       self.imag - other.imag)

    def __mul__(self, other):
        return Complex(self.real * other.real - self.imag * other.imag,
                       self.imag * other.real + self.real * other.imag)

    def __str__(self):
        return '(%g, %g)' % (self.real, self.imag)

    def __repr__(self):
        return 'Complex' + str(self)


complexone = Complex(5, 2)
complextwo = Complex(0, 4)
complexthree = Complex(-6, 2)
complexfour = Complex(3, -2)
additionalcheckreal = 0
additionalcheckimag = 0

print("Операция с классом:", complexone + complexfour)
additionalcheckreal = 5 + 3
additionalcheckimag = 2 - 2
print("Проверка:", additionalcheckreal, additionalcheckimag)

print("Операция с классом:", complexone * complexthree)
additionalcheckreal = (5 * -6) - (2 * 2)
additionalcheckimag = (2 * -6) + (5 * 2)
print("Проверка:", additionalcheckreal, additionalcheckimag)

print("Операция с классом:", complexone * complextwo)
additionalcheckreal = (5 * 0) - (2 * 4)
additionalcheckimag = (2 * 0) + (5 * 4)
print("Проверка:", additionalcheckreal, additionalcheckimag)

print("Операция с классом:", complexfour + complextwo)
additionalcheckreal = 3 + 0
additionalcheckimag = -2 + 4
print("Проверка:", additionalcheckreal, additionalcheckimag)
