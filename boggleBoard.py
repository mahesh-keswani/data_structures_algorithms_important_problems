class Node:

    def __init__(self):
        self.children = {}
        self.endOfWord = '*'

class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word):
        root = self.root
        for letter in word:
            if letter not in root.children:
                root.children[letter] = Node()

            root = root.children[letter]

        root.children['*'] = word

def boggleBoard(board, array):
    trie = Trie()
    for word in array:
        trie.insert(word)

    rows = len(board)
    cols = len(board[0])
    
    visited = [ [False for col in range(cols)] for row in range(rows)]
    finalWords = set()

    for i in range(rows):
        for j in range(cols):
            explore(i, j, board, visited, trie, finalWords, rows, cols)

    return finalWords

    
def explore(i, j, board, visited, trie, finalWords, rows, cols):
    if visited[i][j]:
        return

    letter = board[i][j]
    if letter not in trie.children:
        return

    visited[i][j] = True

    # update the trie level
    trie = trie.children[letter]

    # i.e we have reached the end of word
    if '*' in trie.children:
        finalWord.add( trie.children['*'] )

    # get the neighbors and explore them
    neighbors = getNeighbors(i, j, rows, cols)

    for neighbor in neighbors:
        explore(neighbor[0], neighbor[1], board, visited, trie, finalWords, rows, cols)

    # set the visited to False, as there can be other words which might use the same character
    visited[i][j] = False
    
def isValid(i, j, rows, cols):
    return i >= 0 and i < rows and j >= 0 and j < cols

def getNeighbors(x, y, rows, cols):
    # possible 8 directions
    dx = [-1, -1, -1, 0, 1, 1, 1, 0]
    dy = [-1, 0, 1, 1, 1, 0, -1, -1]

    neigbors = []

    for i in range(8):
        newX = x + dx[i]
        newY = y + dy[i]

        if isValid(newX, newY, rows, cols):
            neighbors.append([newX, newY])

    return neighbors
