def print_operation_table(operation, num_rows=9, num_columns=9):
    for i in range(1, num_rows+1):
        for j in range(1, num_columns+1):
            print(operation(i, j), end=' ')
        print()


print_operation_table(lambda x, y: x*y, 5, 5)
print(*['-' for i in range(40)], sep='')
print_operation_table(lambda x, y: 2**y, 1, 10)
