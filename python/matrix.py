matrix = [[11, 22, 33], [44, 55, 66], [77, 88, 99]]

row_length = len(matrix)
columns_length = len(matrix[0])

print(" ")
for row in range(row_length):
    print(f"ROW({row}):")
    for columns in range(columns_length):
        print(f"[{matrix[row][columns]}]", end=", ")
        print(
            f"K: {row} * {columns_length} + {columns} -> {row * columns_length + columns}"
        )
    print(" ")

