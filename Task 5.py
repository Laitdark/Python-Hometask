class Stationary:
    def get_name(self, stationary_type):
        if stationary_type == 1:
            self.title = "Pen"
        elif stationary_type == 2:
            self.title = "Pencil"
        elif stationary_type == 3:
            self.title = "Handle"
        else:
            self.title = "Undefined"
        print("Наша принадлежность:", self.title)

    def draw(self):
        print("Рисуем нашей канц. принадлежностью")


class Pen(Stationary):

    def draw(self):
        print("Рисуем ручкой")


class Pencil(Stationary):

    def draw(self):
        print("Рисуем карандашом")


class Handle(Stationary):

    def draw(self):
        print("Рисуем маркером")


stationary_type = int(
    input("Введите номер принадлежнсти (1 - ручка, 2 - карандаш, 3 - маркер, другая цифра - не определено): "))
userstationary = ""
if stationary_type == 1:
    userstationary = Pen()
elif stationary_type == 2:
    userstationary = Pencil()
elif stationary_type == 3:
    userstationary = Handle()
else:
    userstationary = Stationary()
userstationary.get_name(stationary_type)
userstationary.draw()
