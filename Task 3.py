class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        print("Полное имя:", self.name, self.surname)

    def get_total_income(self):
        print("Доход с учетом премии:", self._income["wage"] + self._income["bonus"])


journalist = Position("Alex", "Jones", "Journalist", 20000, 10000)
journalist.get_full_name()
journalist.get_total_income()

