import numpy as np

def find_special_elements(matrix):
    rows, cols = matrix.shape
    special_elements = []

    for j in range(cols):
        col_sum = np.sum(matrix[:, j])
        for i in range(rows):
            if matrix[i, j] > col_sum - matrix[i, j]:
                special_elements.append((matrix[i, j], i, j))

    return special_elements

def find_min_special_elements(matrix):
    special_elements = find_special_elements(matrix)
    if not special_elements:
        return []

    min_value = min(special_elements, key=lambda x: (x[0], x[2]))[0]
    min_elements = [(value, row, col) for value, row, col in special_elements if value == min_value]
    return min_elements

# Приклад використання
matrix = np.array([
    [10, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 130, 11, 12],
    [130, 14, 15, 16]
])

min_elements = find_min_special_elements(matrix)

if min_elements:
    print("Мінімальні С-особливі елементи:")
    for element in min_elements:
        value, row, col = element
        print(f"Елемент: {value}")
        print(f"Номер стовпця: {col + 1}")
        print(f"Індекси елемента: ({row + 1}, {col + 1})")
else:
    print("таких нема!")
