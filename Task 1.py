import collections

corp = collections.namedtuple('Corp', 'name quarterone quartertwo quarterthree quarterfour year')

corpcount = int(input('Введите количество предприятий: '))
corps = []
profits = 0

for i in range(corpcount):
    name = input('Введите название ' + str(i + 1) + ' предприятия: ')
    fourquarters = [float(j) for j in input('Введите через запятую в каждом квартале: ').split(',')]
    year = 0
    for quarter in fourquarters:
        year = year + quarter

    profits = profits + year
    corps.append(corp(name, *fourquarters, year))

avgprofit=profits/corpcount
below=[]
above=[]

for i in range(corpcount):
    if corps[i].year>avgprofit:
        above.append(corps[i])
    elif corps[i].year<avgprofit:
        below.append(corps[i])

print('Average profit:',avgprofit)
print('Corps above it:')
for i in above:
    print(i.name, i.year)
print('Corps below it:')
for i in below:
    print(i.name, i.year)