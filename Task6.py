userinput = ""
baselist = []
propertiesdict = {"Название": [], "Цена": [], "К-во": [], "Размерность": []}
count = 1
updatername = []
updatercost = []
updateramount = []
updaterscale = []

while userinput != "end":
    goodname = input("Введите название товара: ")
    goodcost = input("Введите цену товара: ")
    goodamount = input("Введите к-во товара: ")
    goodscale = input("Введите размерность товара: ")
    updatername.append(goodname)
    updatercost.append(int(goodcost))
    updateramount.append(int(goodamount))
    updaterscale.append(goodscale)

    baselist.append((count, {"Название": goodname,
                             "Цена": goodcost,
                             "К-во": goodamount,
                             "Размерность": goodscale
                             }))
    userinput = input("Для окончания ввода введите end: ")
    count += 1

## В корне не согласен с удалением дубликатов здесь. Если убирать дубликаты в каких либо строках, то теряется очевидная взаимосвязь в каталоге
propertiesdict.update({
    "Название": updatername,
    "Цена": updatercost,
    "К-во": updateramount,
    "Размерность": updaterscale
})

print("Список товаров:")
for i in baselist:
    print(i)
print("Каталог товаров:")
print(propertiesdict)
