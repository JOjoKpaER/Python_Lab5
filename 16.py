"""
36
12
144
18
"""

import sys
import math

res = int(input())
for line in sys.stdin:
    if '' == line.rstrip():
        break
    res = math.gcd(res, int(line))
print(res)