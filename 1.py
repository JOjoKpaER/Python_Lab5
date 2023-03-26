lst = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]


def less_than_five(n):
    if n < 5:
        return True
    else:
        return False


def more_than_seventeen(n):
    if n > 17:
        return True
    else:
        return False


def div_by_nine(n):
    if n % 9 == 0 and n > 9:
        return True
    else:
        return False


print(*list(filter(less_than_five, lst)))
print(*list(map(lambda n: n//2, lst)))
print(*list(map(lambda n: n//2, filter(more_than_seventeen, lst))))
print(sum(map(lambda n: n**2, filter(div_by_nine, lst))))