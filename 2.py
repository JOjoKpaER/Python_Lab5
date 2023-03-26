def factorials(n):
    ret = 1
    for i in range(1, n+1):
        ret *= i
        yield ret


for i in factorials(7):
    print(i, end=' ')
print()
for i in factorials(10):
    print(i, end= ' ')
