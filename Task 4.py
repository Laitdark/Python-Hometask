class Car:
    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        self.police = False

    def show_speed(self):
        print("Мы едем со скоростью (км/ч):", self.speed)

    def go(self):
        print("Машина поехала")

    def turn(self, direction):
        print("Машина повернула в направлении:", direction)

    def stop(self):
        print("Машина остановилась")


class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)


class TownCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)

    def show_speed(self):
        print("Мы едем со скоростью (км/ч):", self.speed)
        if self.speed > 60:
            print("Сбавьте скорость, превышаем")


class WorkCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)

    def show_speed(self):
        print("Мы едем со скоростью (км/ч):", self.speed)
        if self.speed > 40:
            print("Сбавьте скорость, превышаем")


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self.police = True


porsche = SportCar(200, "Red", "911")
daewoo = TownCar(65, "Blue", "Lanos")
honda = PoliceCar(90, "White", "Civic")
vazniva = WorkCar(45, "Black", "Niva")
vazold = WorkCar(35, "White", "07")
zaz = TownCar(20, "Green", "ZAZ")

carpark = [porsche, daewoo, honda, vazold, vazniva, zaz]
directions = ["Left", "Right"]

for el in carpark:
    print("Наша машина:", el.name)
    el.go()
    el.turn(directions[0])
    el.turn(directions[1])
    el.show_speed()
    el.stop()
    print("Наша машина полицейская?", el.police)
