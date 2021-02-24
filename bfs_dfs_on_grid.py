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
