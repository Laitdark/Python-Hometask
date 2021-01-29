tasktwofile = open("Task2.txt", 'r', encoding='utf-8')
filelines = tasktwofile.read().splitlines()
print(filelines)
wordcount = []
wordline = []
print("К-во строк: ", len(filelines))
for i in filelines:
    wordline = i.split(" ")
    wordcount.append(len(wordline))
print("К-во слов в каждой строке по порядку: ", wordcount)
tasktwofile.close()
