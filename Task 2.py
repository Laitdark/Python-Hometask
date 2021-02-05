from abc import ABC, abstractmethod


class Clothes(ABC):
    name = "Одежда"

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

    @property
    @abstractmethod
    def fabricusage(self):
        pass


class Coat(Clothes):
    name = "Пальто"

    def __init__(self, size):
        self.size = size

    def __str__(self):
        newstring = self.name + ' размера ' + str(self.size)
        return newstring

    @property
    def fabricusage(self):
        return round(self.size / 6.5 + 0.5, 2)


class Suit(Clothes):
    name = "Костюм"

    def __init__(self, height):
        self.height = height

    def __str__(self):
        newstring = self.name + ' на рост ' + str(self.height)
        return newstring

    @property
    def fabricusage(self):
        return round(self.height * 2 + 0.3, 2)


coat = Coat(60)
suit = Suit(192)
print(coat, "Необходимо ткани:", coat.fabricusage)
print(suit, "Необходимо ткани:", suit.fabricusage)
