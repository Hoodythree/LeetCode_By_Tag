def rotate(matrix):
    # swap row
    start = 0
    end = len(matrix) - 1
    while start < end:
        matrix[start], matrix[end] = matrix[end], matrix[start]
        start += 1
        end -= 1

    # # Transfer
    for i in range(len(matrix)):
        for j in range(i, len(matrix[i])):
            matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]
    return matrix
    

matrix = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]
print(rotate(matrix))
