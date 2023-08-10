def transposeMatrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    # transposed result matrix
    result = [[0 for i in range(rows)] for j in range(cols)]
    for i in range(rows):
        for j in range(cols):
            if i == j:
                result[i][j] = matrix[i][j]
            result[j][i] = matrix[i][j]
    return (f"result --> {result}")


print(transposeMatrix([[1, 2]]))


# the other way of doing it is to tranverse col outer loop and rows inner loop and adding each element
