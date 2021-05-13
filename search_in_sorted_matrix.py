def searchInSortedMatrix(matrix, k):
    row = 0
    col = len(matrix[0])

    while row < len(matrix) and col >= 0:

        if k > matrix[row][col]:
            row += 1
        elif k < matrix[row][col]:
            col -= 1
        else:
            return [row, col]

    return [-1, -1]
