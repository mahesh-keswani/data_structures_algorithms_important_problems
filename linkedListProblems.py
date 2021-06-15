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
	
	def revereseList(self):
		if self is None:
			return 
		
		p1 = None
		p2 = self
      	
		while p2 is not None:
			p3 = p2.next
			p2.next = p1
			p1 = p2
			p2 = p3
	
	# at the end, p1 will be node with the new head of reversed linked list
    return p1
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

# problem is, we have two linkedlist which are sorted respectively, and we have to merge them so that the resultant list is also sorted.
# we are  allowed to mutate list
def mergeTwoLists(head1, head2):
	p1 = head1
	p2 = head2
	p1Prev = None
# 	1   8 -> 13
# 	4 -> 5 -> 9
	while p1 is not None and p2 is not None:
		if p1.value < p2.value:
			p1Prev = p1
			p1 = p1.next
		else:
			if p1Prev is not None:
				p1Prev.next = p2
				
			p1Prev = p2
			p2 = p2.next
			p1Prev.next = p1
	
	# if the list1 is done, then just merge last node of list with the remaining of list2
	if p1 is None:
		p1Prev.next = p2
	
	# return the head with the smallest value
	return head1 if head1.value < head2.value else head2


'''
    Two numbers are represented using two linked list, where each node contains single digit.
    We have to find sum of these two numbers and return the sum list (each digit in one node)
'''

class Node:
    def __init__(self, digit):
        self.digit = digit
        self.next = None

def sumOfTwoLL(head1, head2):
    firstNumber = createNumber(head1)
    secondNumber = createNumber(head2)

    finalSum = firstNumber + secondNumber

    # creating linked list of digits in finalSum
    # 528
    # 5-> 2-> 8
    prev = None
    finalHead = None
    for digit in str(finalSum):
        newNode = Node( int(digit) )

        if prev is None:
            prev = newNode
            finalHead = newNode
        else:
            prev.next = newNode
            prev = newNode

    return finalHead

def createNumber(head):
    node = head
    val = 0
    
    # e.g 5 -> 6 -> 3
    # First iteration: val = 0 + 5 = 5
    # second iteration: val = 50 + 6 = 56
    # third iteration: val = 560 + 3 = 563
    
    while node:
        val = (val * 10) + node.digit
        node = node.next

    return val


'''
    Reverse a linked list in group of k.

    Idea is, first reverse the first k nodes of list, then recursively reverse the next k nodes
    and also keep track of pointer of next node.
    
'''

class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

def reverseLinkedList(head, k):
    if head is None:
        return None

    p1 = None
    p2 = head

    # reverse the linked list upto k nodes
    count = 0
    while p2 is not None and (count < k):
        p3 = p2
        p2.next = p1
        p1 = p2
        p2 = p3

        count += 1

    # i.e further linked list exist
    if p3 is not None:

        # now the head will be last node in group of k, so update it's next recursively.
        # now reverse the list using p3 as head 
        head.next = reverseLinkedList(p3, k)

    # at the end p1 will be head of the list
    return p1
