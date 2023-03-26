def arithmetic_operation(s):
    if s == '+':
        return lambda x, y: x + y
    if s == '-':
        return lambda x, y: x - y
    if s == '*':
        return lambda x, y: x * y
    if s == '/':
        return lambda x, y: x/y


operation = arithmetic_operation('+')
print(operation(1, 4))
operation = arithmetic_operation('-')
print(operation(1, 4))
operation = arithmetic_operation('*')
print(operation(1, 4))
operation = arithmetic_operation('/')
print(operation(1, 4))