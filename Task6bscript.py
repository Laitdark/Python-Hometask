import itertools
from sys import argv

script_name, cycler, end = argv
end = int(end)
counter = 1

for el in itertools.cycle(cycler):
    if counter == end:
        break
    print(el)
    counter += 1
