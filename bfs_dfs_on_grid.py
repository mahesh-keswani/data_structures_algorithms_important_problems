def isValid(newX, newY, visited):
    return newX >=0 and newX < len(visited) and newY >= 0 and newY < len(visited[0]) and not visited[newX][newY] and arr[newX][newY]

def dfs(arr, x, y, visited, cur_size = 1):
    visited[x][y] = True
    # Up = [-1, 0]
    # Right = [0, 1]
    # Down = [1, 0]
    # Left = [0, -1]
    
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    for i in range(4):
        newX = x + dx[i]
        newY = y + dy[i]
        
        if isValid(newX, newY, visited):
            size = dfs(arr, newX, newY, visited, cur_size = 1)
            cur_size += size

    return cur_size

'''
    arr = [
    [1, 0, 0, 1, 1],
    [0, 1, 0, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 1, 1, 0, 1],
    [0, 1, 0, 0, 1]
]
 1 means part of river and 0 means land
 Expected output: [1, 5, 3, 2]

'''
def findingSizeOfEveryRiver(arr):
    rows = len(arr)
    cols = len(arr[0])
    visited = [ [False for col in range(cols)] for row in range(rows) ]
    river_sizes = []
    
    for i in range(rows):
        for j in range(cols):
            if visited[i][j]:
                continue
            elif arr[i][j] == 0:
                visited[i][j] = True
            else:
                count = dfs(arr, i, j, visited)
                river_sizes.append(count)

    return river_sizes

# Counting the number of islands in grid
'''
    arr = [
    [1, 0, 0, 1, 1],
    [0, 1, 0, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 1, 1, 0, 1],
    [0, 1, 0, 0, 1]
]
 1 means part of island and 0 means river
 Expected output: 4

 Idea is, use the code for finding the river sizes, and the length of the river_sizes will be = number of islands
'''
def numberOfIslands(arr):
    islands_sizes = findingSizeOfEveryRiver(arr)
    return len(islands_sizes)

# =======================================================================================================

def isValidNode(x, y, arr, visited):
    return x >=0 and x < len(visited) and y >= 0 and y < len(visited[0]) and not visited[x][y] and (arr[x][y] == 'P' or arr[x][y] == 'E')

# By default assuming the valid directions are up, right, down, left, and also makking validation function as paramter
def bfs(arr, x, y, visited, distances, dx = [-1, 0, 1, 0], dy = [0, 1, 0, -1], validationFunc = isValidNode):
    queue = [ [x, y] ]
    distances[x][y] = 0
    visited[x][y] = True

    while len(queue):
        currentNode = queue.pop(0)
        x = currentNode[0]
        y = currentNode[1]
        d = distances[x][y]

        for i in range(4):
            newX = x + dx[i]
            newY = y + dy[i]

            if isValidNode(newX, newY, arr, visited):
                distances[newX][newY] = d + 1
                visited[newX][newY] = True
                queue.append( [newX, newY] )
    
'''
    arr = [
    ['S', 'P', 'P', 'P', 'P'],
    ['T', 'P', 'T', 'P', 'P'],
    ['T', 'P', 'P', 'P', 'P'],
    ['P', 'T', 'E', 'T', 'T'],
    ['P', 'T', 'P', 'T', 'T']

    S = Source, T = tree, E = End, P = path, we can only travel through P
    Task: To find out shortest path from [0,0] to [3,2]
    # Expected output: 5
'''
def findShortestPathFromSourceToDest(arr, srcx, srcy, destx, desty):
    rows = len(arr)
    cols = len(arr[0])

    visited = [ [False for col in range(cols)] for row in range(rows)]
    distances = [ [0 for col in range(cols)] for row in range(rows) ]

    bfs(arr, srcx, srcy, visited, distances)

    return distances[destx][desty]

# =======================================================================================================

def validFuncForKnight(x, y, arr, visited):
    return x >=0 and x < len(visited) and y >= 0 and y < len(visited[0]) and not visited[x][y]

'''
    arr = [
    [0,  0, 0, 0,  T,  0],
    [0,  S, 0, 0,  0,  0],
    [0,  0, 0, 0,  0,  0],
    [0,  0, 0, 0,  0,  0],
    [0,  0, 0, 0,  0,  0],
    [0,  0, 0, 0,  0,  0]    
]
    Expected output: 2

'''

def findMinMovesForKnightToMoveFromSrcToDest(arr, srcx, srcy, destx, desty):
    rows = len(arr)
    cols = len(arr[0])

    visited = [ [False for col in range(cols)] for row in range(rows)]
    distances = [ [0 for col in range(cols)] for row in range(rows) ]

    # If at any time, knight is at position [x, y], then these are the valid moves for the knight
    dx = [-2, -1, 1, 2, 2, 1, -1, -2]
    dy = [1, 2, 2, 1, -1, -2, -2, -1]
    bfs(arr, srcx, srcy, visited, distances, dx = dx, dy = dy, validationFunc = validFuncForKnight)
        
    return distances[destx][desty]
    
# ======================================================================================================

def isValidXO(matrix, i, j):
    return i >= 0 and i < len(matrix) and j >= 0 and j < len(matrix[0]) and matrix[i][j] == 'O'

def dfsOnXO(matrix, x, y):
    # Ind means invalid
    matrix[x][y] = 'Ind'

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    for i in range(4):
        newX = x + dx[i]
        newY = y + dy[i]

        if isValidXO(matrix, newX, newY):
            dfsOnXO(matrix, newX, newY)

def convertOsToXWhichAreCompletelySurroundedByX(matrix):
    '''
        Idea is, traverse all the boundries, and at every boundry if O is encountered, then it means this is not valid
        O (as it is not surrounded by X in all four directions), therefore mark it as invalid, also mark all the O's
        associated with it as invalid using dfs
    '''
    rows = len(matrix)
    cols = len(matrix[0])
    
    # top row
    for i in range(0, cols):
        if matrix[0][i] == 'O':
            # matrix, i, j
            dfsOnXO(matrix, 0, i)

    # last column
    for i in range(0, rows):
        if matrix[i][cols - 1] == 'O':
            dfsOnXO(matrix, i, cols - 1)

    # bottom row
    for i in range(0, cols):
        if matrix[rows - 1][i] == 'O':
            dfsOnXO(matrix, rows - 1, i)

    # left column
    for i in range(0, rows):
        if matrix[i][0] == 'O':
            dfsOnXO(matrix, i, 0)


    # Now all the invalid O's will be marked as Invalid, therefore we have to now convert all the valid O's to X
    # and mark again back the Invalid as O
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 'Ind':
                matrix[i][j] = 'O'
            elif matrix[i][j] == 'O':
                matrix[i][j] = 'X'

    for row in matrix:
        print(row)

matrix = [
    ['X', 'O', 'X', 'X', 'X', 'X'],
    ['X', 'O', 'X', 'X', 'O', 'X'],
    ['X', 'X', 'X', 'O', 'O', 'X'],
    ['O', 'X', 'X', 'X', 'X', 'X'],
    ['X', 'X', 'X', 'O', 'X', 'O'],
    ['O', 'O', 'X', 'O', 'O', 'O']
]

convertOsToXWhichAreCompletelySurroundedByX(matrix)

def wordSearch(board, word):
    rows = len(board)
    cols = len(board[0])

    if rows == 0 or cols == 0:
        return False

    visited = [ [False for col in range(cols)] for row in range(rows)]
    isFound = False
    for i in range(rows):
        for j in range(cols):
            isFound = explore(i, j, board, visited, rows, cols, word, 0)

            if isFound:
                return True

    return False

def isValidPosition(i, j, rows, cols):
    return 0 <= i < rows and 0 <= j < cols

def explore(x, y, board, visited, rows, cols, word, idx):
    if visited[x][y]:
        return

    letter = board[x][y]
    if letter != word[idx]:
        return False

    visited[x][y] = True
    
    if idx == (len(word) - 1):
        return True

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    for i in range(4):
        newX = x + dx[i]
        newY = y + dy[i]

        if isValidPosition(newX, newY, rows, cols):
            explore(newX, newY, board, visited, rows, cols, word, idx + 1)
            
    visited[x][y] = False
