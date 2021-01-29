translationdict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
taskfourfile = open("Task4.txt", 'r', encoding='utf-8')
filelines = taskfourfile.read().splitlines()
templist = []
newfilelines = []
for i in filelines:
    templist = i.split(" ")
    i = ""
    templist[0] = translationdict[templist[0]]
    i = " ".join(templist)
    newfilelines.append(i)
print(newfilelines)
taskfourfile.close()
with open('Task4translated.txt', 'tw', encoding='utf-8') as taskfourfile:
    for i in newfilelines:
        taskfourfile.write(i + "\n")
taskfourfile.close()