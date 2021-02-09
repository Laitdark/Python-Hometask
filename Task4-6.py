class Warehouse():
    def __init__(self, name):
        self.name = name
        self.items = {}

    def __str__(self):
        strres = "Состояние склада: " + self.name + "\n"
        if self.items:
            strres = strres + str(self.items)
        else:
            strres = strres + "На складе ничего нет"
        return strres

    def addequipment(self, equipment, amount):
        if not type(amount) is int:
            raise ValueError
        else:
            if not equipment in self.items:
                self.items[equipment] = amount
            else:
                self.items[equipment] = self.items[equipment] + amount

    def removeequipment(self, equipment, amount):
        if not type(amount) is int:
            raise ValueError
        else:
            if not equipment in self.items:
                raise KeyError(equipment)
            elif self.items[equipment]==0:
                raise KeyError(equipment)
            else:
                self.items[equipment] = self.items[equipment] - amount

    def moveequipment(self, equipment, amount, destination):
        if not type(amount) is int:
            raise ValueError
        else:
            self.removeequipment(equipment, amount)
            destination.addequipment(equipment, amount)


class Equipment():
    def __init__(self, model, year, weight):
        if not (type(year) is int or (year >= 1 and year <= 2500)):
            raise ValueError("Год заполнен некорректно")
        if not ((type(weight) is int or type(weight) is float) and weight > 0):
            raise ValueError('Вес заполнен некорректно')

        self.model = model
        self.year = int(year)
        self.weight = float(weight)

    def __str__(self):
        tempstring = "Название устройства: " + self.itemname + ", Модель: " + self.model + ", Вес: " + str(
            self.weight) + ", Год выпуска: " + str(self.year)
        return tempstring

    def shorten(self):
        tempstring = self.itemname + "-" +self.model
        return tempstring


class Printer(Equipment):
    itemname = 'Принтер'


class Scanner(Equipment):
    itemname = 'Сканер'


class Xerox(Equipment):
    itemname = 'Ксерокс'


firstwarehouse = Warehouse("Склад 1")
secondwarehouse = Warehouse("Склад 2")
equipmentone = Printer("LG", 2020, 12)
equipmenttwo = Scanner("Canon", 2016, 6)
equipmentthree = Xerox("Xerox", 2010, 9)
equipmentfour = Xerox("Old Xerox", 2000, 10)
print("Наши устройства:\n", equipmentthree, "\n", equipmenttwo, "\n", equipmentone)
firstwarehouse.addequipment(equipmentone.shorten(), 20)
firstwarehouse.addequipment(equipmentthree.shorten(), 25)
firstwarehouse.addequipment(equipmenttwo.shorten(), 15)
print("\n", firstwarehouse, "\n", secondwarehouse)
print("\nПроведем передвижения\n")
firstwarehouse.removeequipment(equipmentthree.shorten(),15)
firstwarehouse.moveequipment(equipmenttwo.shorten(),15,secondwarehouse)
firstwarehouse.moveequipment(equipmentone.shorten(),20,secondwarehouse)
print("", firstwarehouse, "\n", secondwarehouse)
print("\nПопробуем выдать ошибки\n")
try:
    firstwarehouse.removeequipment(equipmentfour.shorten(), 10)
except ValueError:
    print("Некорректное значение")
except KeyError:
    print("Ошибка операции")
try:
    firstwarehouse.removeequipment(equipmenttwo.shorten(), "Food")
except ValueError:
    print("Некорректное значение")
except KeyError:
    print("Ошибка операции")
try:
    secondwarehouse.removeequipment(equipmentone.shorten(), 10)
except ValueError:
    print("Некорректное значение")
except KeyError:
    print("Ошибка операции")

print("\n", firstwarehouse, "\n", secondwarehouse)
