"""
Ехал Грека через реку
Видит Грека в реке рак
Сунул в реку руку Грека
Рак за руку Греку цап
"""

import sys

inpt = []
for line in sys.stdin:
    if '' == line.rstrip():
        break
    inpt.extend(line.split())
out = []
for count, value in enumerate(inpt):
    out.append([count, value])
out = sorted(out, key=lambda x: x[1])
pr = []
pr1 = []
for i in out:
    if i[1][0].isupper() and i[1] not in pr1:
        pr.append(i)
        pr1.append(i[1])
print(*pr, sep='\n')
