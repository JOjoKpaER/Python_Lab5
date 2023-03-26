lst = [3, 6, -8, 2, -78, 1, 23, -45, 9]

print(*sorted(lst, key=abs, reverse=True))