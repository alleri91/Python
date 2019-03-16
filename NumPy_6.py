import numpy as np

image_matrix = np.matrix([[0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0]])
print(image_matrix)



rows = image_matrix.shape[0]
columns = image_matrix.shape[1]
print(rows)
print(columns)


for row in range(rows):
    for column in range(columns):
        if image_matrix[row, column] == 0:
            image_matrix[row, column] = 1
        else:
            image_matrix[row, column] = 0



print(image_matrix)

print(image_matrix.transpose())
