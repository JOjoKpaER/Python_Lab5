"""
котик
тюлень
кашалот
нарвал
"""

from functools import reduce
import sys

inpt = []
for line in sys.stdin:
    if '' == line.rstrip():
        break
    inpt.append(line.strip())

print(reduce(min, inpt))
