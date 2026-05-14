matrix = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]

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

