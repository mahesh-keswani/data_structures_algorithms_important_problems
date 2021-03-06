class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

class SinglyLL:
    def __init__(self):
        self.head = None

    def insert(self, value):
        newNode = Node(value)

        if self.head is None:
            self.head = newNode
        else:
            currentNode = self.head
            while currentNode.next is not None:
                currentNode = currentNode.next
            
            currentNode.next = newNode
        return self

    def printList(self):
        node = self.head
        while node:
            print(node.value)
            node = node.next

    # staring -> starting of loop and ending => ending of loop 
    def createLoop(self, starting, ending):
        if self.head is None:
            return

        # For keeping track of starting and ending Nodes
        startingNode = None
        endingNode = None
        
        node = self.head
        while node is not None:
            if node.value == starting:
                startingNode = node

            if node.value == ending:
                endingNode = node

            node = node.next

        # adding loop here
        endingNode.next = startingNode
                
'''
    1-2-3-4-5-6
            |  |
            8-7
'''

singlyLL = SinglyLL()

singlyLL.insert(1).insert(2).insert(3).insert(4).insert(5).insert(6).insert(7).insert(8)

# singlyLL.printList()

singlyLL.createLoop(5, 8)
# singlyLL.printList()
