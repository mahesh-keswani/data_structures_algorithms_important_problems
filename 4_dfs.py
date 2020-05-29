class Node:

    def __init__(self, name):
        self.name = name
        self.children = []

    def addChild(self, name):
        self.children.add(Node(name))
        
##  this array parameter will contain the nodes in the order in which dfs will traverse  
    def dfs(self, array):
        array.append(self.name)
        for child in self.children:
            child.dfs(array)

        return array
