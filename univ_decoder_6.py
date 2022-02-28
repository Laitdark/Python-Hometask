from chardet import detect

with open('test_file.txt', 'rb') as fl:
    content = fl.read()
    ENCODING=detect(content)['encoding']

with open('test_file.txt', 'r', encoding=ENCODING) as fl:
    content = fl.read()
    print(content)