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

    def detectLoop(self):
        if self.head is None:
            return

        p = self.head
        q = self.head

        # if p is none or q is none or q.next is none then there is no loop in the list
        while p is not None and q is not None and q.next is not None:
            p = p.next
            q = q.next.next
            
            if p == q:
                return p
            
        # if loop is present, then p will be returned, else one of the above condition will fail and will return False
        return False
    
    def detectStartOfLoop(self):
        p = self.detectLoop()
        if not p:
            return "No loop present"

        q = self.head
        while p != q:
            q = q.next
            p = p.next

        return p

        
    def removeLoop(self):
        p = self.detectLoop()
        if not p:
            return "No loop present"

        q = self.head
        while True:
            q = q.next

            if p.next == q:
                break
            p = p.next

        p.next = None
    
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

print( singlyLL.detectLoop().value )

print(singlyLL.detectStartOfLoop().value)

singlyLL.removeLoop()
singlyLL.printList()
