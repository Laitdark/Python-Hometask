taskthreefile = open("Task3.txt", 'r', encoding='utf-8')
filelines = taskthreefile.read().splitlines()
print(filelines)
templist = []
sumofsalaries = 0
print("Оклады меньше 20 000 UAH: ")
for i in filelines:
    templist = i.split(" ")
    if int(templist[1]) < 20000:
        print(templist[0], templist[1])
    sumofsalaries = sumofsalaries + int(templist[1])
averagesalary = sumofsalaries / len(filelines)
print("Средняя зарплата: ", averagesalary)
taskthreefile.close()