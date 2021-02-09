import ast


class StrOrBoolException(Exception):
    def __str__(self):
        return "Нельзя вводить строки и булевые значения"


def checktypetoappend(x, userlist):
    if type(x) is str or type(x) is bool:
        raise StrOrBoolException
    else:
        userlist.append(x)


templist = []
userinput = ""
while userinput != "stop":
    x = input("Введите элемент списка (Для окончания введите stop): ")
    try:
        userinput = ast.literal_eval(x)
    except ValueError:
        userinput = x
    if userinput != "stop":
        try:
            checktypetoappend(userinput, templist)
        except StrOrBoolException as e:
            print(e)

print("Наш список:", templist)
