import json
tasksevenfile = open("Task7.txt", 'r', encoding='utf-8')
filelines = tasksevenfile.read().splitlines()
templist = []
firmdict = {}
profitdict = {"AvgProfit": 0}
firmcount = 0
firmprofit = 0
for i in filelines:
    templist = i.split(" ")
    profit = int(templist[2]) - int(templist[3])
    if profit > 0:
        firmcount += 1
        firmprofit = profit + firmprofit
    firmdict[templist[0]] = str(profit)
averageprofit = firmprofit / firmcount
profitdict["AvgProfit"] = str(averageprofit)
newlist = [firmdict, profitdict]
tasksevenfile.close()
with open('Task7.json', 'tw', encoding='utf-8') as tasksevenfile:
    json.dump(newlist,tasksevenfile)
tasksevenfile.close()
