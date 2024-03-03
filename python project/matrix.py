import random

def generate_random_matrix(rows, cols):
    matrix = []
    for _ in range(rows):
        row = [random.randint(1, 100) for _ in range(cols)]
        matrix.append(row)
    return matrix

def get_column_sum(matrix, col_index):
    column_sum = 0
    for row in matrix:
        column_sum += row[col_index]
    return column_sum

def get_row_average(matrix, row_index):
    row = matrix[row_index]
    row_sum = sum(row)
    row_average = row_sum / len(row)
    return row_average


rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

matrix = generate_random_matrix(rows, cols)

print("Generated Matrix:")
for row in matrix:
    print(row)

col_index = int(input(f"Enter the column index (0 to {cols-1}): "))

column_sum = get_column_sum(matrix, col_index)
print(f"Sum of column {col_index}: {column_sum}")

row_index = int(input(f"Enter the row index (0 to {rows-1}): "))

row_average = get_row_average(matrix, row_index)
print(f"Average of row {row_index}: {row_average}")
