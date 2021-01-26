import itertools
from sys import argv

script_name, n, end = argv
n = int(n)
end = int(end)

if n % 2 != 0:
    n = n + 1

for el in itertools.count(n, 2):
    if el > end:
        break
    else:
        print(el)
