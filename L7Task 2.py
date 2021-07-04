import random

def merge(userarray):
    if len(userarray) > 1:
        center = len(userarray) // 2
        left = userarray[:center]
        right = userarray[center:]

        merge(left)
        merge(right)

        i, j, k = 0, 0, 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                userarray[k] = left[i]
                i += 1
            else:
                userarray[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            userarray[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            userarray[k] = right[j]
            j += 1
            k += 1
        return userarray


arraylength = 10
lowborder = 0
highborder = 49
array = [random.randint(lowborder, highborder) for _ in range(arraylength)]

print('Base array:', array)
merge(array)
print('New array:', array)