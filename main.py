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

def find_min_special_element(matrix):
    special_elements = find_special_elements(matrix)
    if not special_elements:
        return None, None, None, None

    min_element, min_row, min_col = min(special_elements, key=lambda x: (x[0], x[2]))
    return min_element, min_row, min_col, min_col + 1

# Приклад використання
matrix = np.array([
    [10, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 100, 11, 12],
    [130, 14, 15, 16]
])

min_element, min_row, min_col, col_number = find_min_special_element(matrix)

if min_element is not None:
    print(f"Мінімальний С-особливий елемент: {min_element}")
    print(f"Номер стовпця: {col_number}")
    print(f"Індекси елемента: ({min_row+1}, {min_col+1})")
else:
    print("таких нема!")
