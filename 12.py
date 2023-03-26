import math

coord = [[5, 1], [4, 2], [3, 3], [2, 4], [5, 1], [6, 0]]

print(sorted(coord, key=lambda x: math.sqrt(x[0]**2 + x[1]**2), reverse=True))
