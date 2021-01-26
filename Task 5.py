import functools


def productfunc(prev_el, el):
    return prev_el * el


evenlist = [i for i in range(99, 1001) if i % 2 == 0]
print(evenlist)
listproduct = functools.reduce(productfunc, evenlist)
print(listproduct)
