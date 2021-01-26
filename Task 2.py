baselist = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print(baselist)
newlist = [next_el for el, next_el in zip(baselist, baselist[1:]) if next_el > el]
print(newlist)
