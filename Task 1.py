import time


class TrafficLight:
    __colour = None
    _colours = ["Red", "Green", "Yellow"]

    def running(self, repeatammount):
        i = 0
        while i < repeatammount:
            self._colour = self._colours[0]
            print("На светофоре красный")
            time.sleep(7)
            self._colour = self._colours[2]
            print("На светофоре желтый")
            time.sleep(2)
            self._colour = self._colours[1]
            print("На светофоре зеленый")
            time.sleep(9)
            i += 1
        print("Цикл завершен")


trafficvariable = TrafficLight()
repeatammount = int(input("Введите к-во повторов цикла светофора: "))
trafficvariable.running(repeatammount)
