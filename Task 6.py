tasksixfile = open("Task6.txt", 'r', encoding='utf-8')
filelines = tasksixfile.read().splitlines()
maindict = {}
templist = []
for i in filelines:
    sum = 0
    templist = i.split(" ")
    for k in templist:
        try:
            int(k) / 1
        except ValueError:
            k = 0
        sum = int(k) + sum
    maindict[templist[0]] = str(sum)
print(maindict)
tasksixfile.close()
