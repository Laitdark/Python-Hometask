import locale

print(locale.getpreferredencoding())
##cp1251

with open('test_file.txt', 'rb') as fl:
    s = fl.read().decode(encoding="utf-8")
    print(s)