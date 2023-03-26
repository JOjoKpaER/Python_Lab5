def same_by(characteristic, objects):
    if len(objects) <= 1:
        return True
    prev = objects[0]
    for i in objects[1:-1]:
        if characteristic(i) != characteristic(prev):
            return False
        prev = i
    return True


val = [0, 2, 10, 6]
if same_by(lambda x: x % 2, val):
    print(True)
else:
    print(False)

values = [1, 2, 3, 4, 5]
if same_by(lambda x: x**2, values):
    print(True)
else:
    print(False)