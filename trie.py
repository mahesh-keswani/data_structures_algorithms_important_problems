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
    
    def countStringWithGivenPrefix(self, prefix):
        root = self.root
        for letter in prefix:
            if letter not in root.children:
                # i.e the given prefix is not present in the trie
                return -1

            root = root.children[letter]

        return len(root.children)
