import binascii

def bytify(string):
    string=bytes(string, 'utf-8')
    return string

def bytifyascii(string):
    string = bytes(string, 'ASCII')
    return string

strs = ['class', 'function', 'method']

for s in strs:
    s=bytify(s)
    print(type(s), binascii.hexlify(s), len(s))
for s in strs:
    s=bytifyascii(s)
    print(type(s), binascii.hexlify(s), len(s))

