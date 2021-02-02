class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width
        self._requiredasphalt = 25
        self._roadgirth = 5

    def asphaltmassammount(self):
        asphaltmass = (self._length * self._width * self._requiredasphalt * self._roadgirth) / 1000
        print("Необоходимо", int(asphaltmass), "т асфальта (При ", self._requiredasphalt,
              "кг асфальта на 1 кв.метр и", self._roadgirth, "см толщины полотна).")


userlength = int(input("Введите длину дороги (в метрах): "))
userwidth = int(input("Введите ширину дороги (в метрах): "))
userroad = Road(userlength, userwidth)
userroad.asphaltmassammount()
