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

def bfs(arr, x, y, visited, distances):
    queue = [ [x, y] ]
    distances[x][y] = 0
    visited[x][y] = True

    while len(queue):
        currentNode = queue.pop(0)
        x = currentNode[0]
        y = currentNode[1]
        d = distances[x][y]

        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]
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








