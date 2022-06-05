def setZeros(matrix):
    row = len(matrix)
    col = len(matrix[0])
    zerothColumn = True
    for i in range(row):
        if matrix[i][0] == 0:
            zerothColumn = False
        for j in range(1, col):
            if matrix[i][j] == 0:
                matrix[i][0] = matrix[0][j] = 0
    for i in range(row - 1, -1, -1):
        for j in range(col - 1, 0, -1):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0
            if zerothColumn == False:
                matrix[i][0] = 0