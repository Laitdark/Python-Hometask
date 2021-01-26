baselist = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print(baselist)
newlist = [el for el in baselist if baselist.count(el) == 1]
print(newlist)