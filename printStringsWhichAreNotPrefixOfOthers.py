class Node:

    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word):
        root = self.root

        for letter in word:
            if letter not in root.children:
                root.children[letter] = Node()

            root = root.children[letter]

            # if the prefix already exists in the trie, then remove it by simply making it's endOfWord as False.
            # and insert the new string. E.g if 'app' already exists in trie and new word is apple, then
            # remove the app and insert the  apple.
            
            if root.endOfWord:
                root.endOfWord = False

        root.endOfWord = True

    def search(self, word):
        root = self.root
        for letter in word:
            if letter not in root.children:
                return False

            root = root.children[letter]

        return root.endOfWord

    def startsWith(self, prefix):
        root = self.root
        for letter in prefix:
            if letter not in root.children:
                return False

            root = root.children[letter]

        return True

    def dfs(self, node, soFar = ''):
        if node.endOfWord:
            print( soFar )
            return

        # else if the word is not ended yet
        for key in node.children.keys():
            self.dfs( node.children[key], soFar + key )
        
'''
    Idea is, consider one string at a time, if the current string is prefix of any other string in trie, then simply
    ignore it (e.g apple is in the trie, and current string is app, so ignore app).
    If the app (prefix) is inserted first in the trie, then the apple comes, then simply make endOfWord of app as False
    and insert the apple.
    +
    
'''
def printStringWhichAreNotPrefixOfOthers(array):
    trie = Trie()
    for word in array:
        # if the current word is prefix of any other word in trie, then simple ignore it
        if trie.startsWith(word):
            continue

        # if the word is not prefix of any other string in the trie, then insert it into trie 
        trie.insert(word)
	
	# perform the dfs inorder to print all the strings in trie
    trie.dfs( trie.root )

array = ['apple', 'app', 'ball']

printStringWhichAreNotPrefixOfOthers( array )
   
