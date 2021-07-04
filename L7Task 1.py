import random


def bubble(userarray):
    n = 1

    while n < len(userarray):
        count = 0

        for i in range(len(userarray) - 1 - (n - 1)):

            if userarray[i] < userarray[i + 1]:
                userarray[i], userarray[i + 1] = userarray[i + 1], userarray[i]
                count += 1

        if count == 0:
            break

        n += 1


arraylength = 10
lowborder = -100
highborder = 99
array = [random.randint(lowborder, highborder) for _ in range(arraylength)]

print('Base array:', array)
bubble(array)
print('New array:', array)