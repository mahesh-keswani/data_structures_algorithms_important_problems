class LRU:

    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.cache = {}
        self.currentSize = 0
        self.list = DoublyLL()

    def insert(self, key, value):
        if key not in self.cache:
            if self.currentSize == self.maxSize:
                self.removeLeastRecent()
            else:
                self.currentSize += 1

            self.cache[key] = Node(key, value)

            # set the newly added node as most recent (head of the list)
            self.list.setHead( self.cache[key] )
            
        else:
            # if key exists then update it's value
            self.cache[key].value = value

    def removeLeastRecent(self):
        # get the key of tail (which contains least recent)
        key = self.list.tail.key

        # delete that entry from cache as well
        del self.cache[key]

        # delete the node (value of the key in cache)
        self.list.removeTail()

    def getKey(self, key):
        if key not in self.cache:
            return None
        # if the key is present in the cache, then set this key as most recent (head)
        self.list.setHead( self.cache[key] )
        return self.cache[key].value

class DoublyLL:

    def __init__(self):
        self.head = None
        self.tail = None

    def setHead(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            return

        if self.head == self.tail:
            self.tail.prev = node
            node.next = self.tail
            self.head = node
        else:
            node.prev.next = node.next
            node.next.prev = node.prev

            node.prev = None
            self.head.prev = node
            node.next = self.head
            self.head = node
            
    def removeTail(self):
        if self.head is None:
            return
        if self.head == self.tail:
            del self.head
        else:

            self.tail.prev.next = None
            secondLastNode = self.tail.prev
            self.tail.prev = None
            
            self.tail = secondLastNode

        
class Node:

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
