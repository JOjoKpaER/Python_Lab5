def alphabet():
    a = ord('а')
    ya = ord('я')
    for i in range(a, ya + 1):
        yield chr(i)


for k in alphabet():
    print(k, end=' ')
