strs = ['разработка', 'сокет', 'декоратор']
strs_in_bytes = []

for s in strs:
    s = s.encode('utf-8', errors='namereplace')
    strs_in_bytes.append(s)
    print(s)

for s in strs_in_bytes:
    print(s.decode('utf-8', errors='replace'))
