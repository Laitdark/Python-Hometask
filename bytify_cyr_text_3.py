##from bytes_2 import bytify, bytifyascii
##for s in strs:
##    bytify(s)

##for s in strs:
##    bytifyascii(s)

##По УТФ-8 не пробивается только Type, без ошибки, по Аски не пробиваются Функция и Класс, код ошибки ниже
##Traceback (most recent call last):
## File "D:\PythoLessons\Course3Lesson1\Lib\bytify_cyr_text_3.py", line 9, in <module>
##    bytifyascii(s)
##  File "D:\PythoLessons\Course3Lesson1\Lib\bytes_2.py", line 8, in bytifyascii
##    string = bytes(string, 'ASCII')
##UnicodeEncodeError: 'ascii' codec can't encode characters in position 0-6: ordinal not in range(128)


strs = ['attribute', 'функция', 'класс', 'type']

for s in strs:
    try:
        bytes(s,'ascii')
    except UnicodeEncodeError:
        print('Слово',s,'невозможно записать')