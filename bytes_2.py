import binascii

##def bytify(string):
##    string=bytes(string, 'utf-8')
##    return string

##def bytifyascii(string):
##    string = bytes(string, 'ASCII')
##    return string


##for s in strs:
##    s=bytify(s)
##    print(type(s), binascii.hexlify(s), len(s))
##for s in strs:
##   s=bytifyascii(s)
##   print(type(s), binascii.hexlify(s), len(s))

str_a = 'class'
str_b = 'function'
str_c = 'method'
strs = [str_a, str_b, str_c]

for el_str in strs:
    el = eval(f"'b'{el_str}'")
    print(type(el), el, len(el))
