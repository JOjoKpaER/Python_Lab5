def square_fibonacci(n):
    n0 = 1
    n1 = 1
    yield n0
    yield n1
    for k in range(2, n):
        n2 = n0 + n1
        yield n2
        n0, n1 = n1, n2


for i in square_fibonacci(7):
    print(i**2, end=' ')
print()
for i in square_fibonacci(10):
    print(i**2, end=' ')
