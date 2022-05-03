from sys import argv

script_name, bonus, time, rate = argv
salary = float(bonus) + (float(time) * float(rate))

print("Премия: ", bonus)
print("Время: ", time)
print("Ставка: ", rate)
print("Оклад: ", salary)
