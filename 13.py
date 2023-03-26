import random

n = 5
m = 5
table = [[random.randint(0, 9) for j in range(m)] for i in range(n)]
print(table)

print(not all([all(i) for i in table]))
