if __name__ == '__main__':
    pass

typelist = ["Hello", 8.2, 8, True, [], {}, ()]
listlength = len(typelist)
i = 0
while i < listlength:
    print(type(typelist[i]))
    i += 1
