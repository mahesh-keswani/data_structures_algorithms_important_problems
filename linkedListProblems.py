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


'''
    Rearrange the given linked list into the following manner:
    given: n1 -> n2 -> n3 -> ... -> nn
    expected: n1 -> nn -> n2 -> nn-1 -> n3 -> nn-3...

    Idea is: get the middle node of list, divide the list into first and second half, reverse
    the second half, the keep addding one node from first and from second alternatively.
'''
class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

def getMiddle(head):
    p = head
    q = head.next

    # while the q exists and q.next exists
    while q and q.next:
        p = p.next
        q = q.next.next

    return p

def reverse(head):
    p1 = None
    p2 = head

    while p2 is not None:
        p3 = p2
        p2.next = p1
        p1 = p2
        p2 = p3

    return p1

def rearrange(head):
    # i.e if list is empty OR list contains only one node OR list contains only two nodes
    # then you cannot rearrange in the required way, so simply return head
    
    if head is None or head.next is None or head.next.next is None:
        return head

    p = getMiddle(head)

    # secondList if the head of second list
    secondList = p.next
    firstList = head

    # set middle.next to None, so the two lists are seperate
    p.next = None

    secondListReversed = reverse(secondList)

    # create a temporary node for creating the new list
    newNode = Node(0)
    currentNode = newNode

    while firstList is not None or secondListReversed is not None:

        if firstList:
            currentNode.next = firstList
            currentNode = currentNode.next
            firstList = firstList.next

        if secondListReversed:
            currentNode.next = secondListReversed
            currentNode = currentNode.next
            secondListReversed = secondListReversed.next

    # the head of the new linkedList
    return newNode.next

'''
    Idea is, we will reverse both the numbers (linked list) and start adding the nodes one by one,
    if carry is generated, then pass on to the next sum, and at the end you will get the whole sum,
    but in the reverse order, so again reverse it.
    There is one edge case, if both the linked list are empty and still carry is non-zero, then
    add it to the result as well, before reversing. (e.g 99 + 1)
'''

def reverse(head):
    if head is None:
        return None

    p1 = None
    p2 = head

    while p2 is not None:
        p3 = p2.next
        p2.next = p1
        p1 = p2
        p2 = p3

    return p1

def addTwoNumbersAsLinkedList(head1, head2):
    first = reverse(head1)
    second = reverse(head2)

    carry = 0
    
    # for creating new list
    newHead, prev = None, None
    
    while first or second:
        # curSum = carry + first.value + second.value
        curSum = carry
        if first:
            curSum += first.value
            first = first.next

        if second:
            curSum += second.value
            second = second.next

        carry = curSum // 10
        curSum = curSum % 10

        newNode = Node(curSum)
        
        if newHead is None:
            newHead = newNode
        else:
            prev.next = newNode

        prev = newNode

    # at the end if carry exist
    if carry:
        newNode = Node(carry)
        prev.next = newNode
        prev = newNode

    # get the actual sum
    resultHead = reverse(newHead)
    return resultHead

'''
    Idea is, first we will find the length of both numbers, (456, 23 | in this case 3, 2), then
    compute the difference of length (in example, diff=1) (make sure that first list is larger one),
    then move `diff` steps ahead in first list and start adding the nodes (i.e start adding 56 and 23),
    using recursion.
'''

def calSum(head1, head2, data):
    # i.e we have reached the end of the lists
    if head1 is None:
        return

    # recursively store the nodes on the call stack
    calSum(head1.next, head2.next, data)
    
    curSum = data['carry'] + head1.value + head2.value

    # update the carry
    data['carry'] = curSum // 10

    newNode = Node(curSum % 10)

    # this result will be head of our sum list
    if data['result'] is None:
        data['result'] = newNode
    else:
        newNode.next = data['result']
        data['result'] = newNode
        
def getLength(head):
    if head is None:
        return 0

    count = 0
    temp = head

    while temp:
        count += 1
        temp = temp.next

    return count

def addRestNodes(head, temp, data):
    # go upto the difference number of nodes
    if head.next == temp:
        return

    addRestNodes(head.next, temp, data)

    curSum = data['carry'] + head.value

    newNode = Node(curSum % 10)
    data['carry'] = curSum // 10

    newNode.next = data['result']
    data['result'] = newNode
    
def addLists(head1, head2):
    first = head1
    second = head2
    
    n1 = getLength(first)
    n2 = getLength(second)
    
    data = {"result": None, "carry": 0}
    
    if n1 == n2:
        calSum(first, second, data)
    else:

        # if the first list is smaller than the second list, then swap the pointers
        # so that first always points to larger list.
        if n1 < n2:
            first, second = second, first

        # calculate the difference in length
        difference = abs(n1 - n2)

        # now move the `difference` steps ahead 
        temp = first
        while difference > 0:
            temp = temp.next
            difference -= 1

        # now temp will point to (d+1)th node
        # now from (d+1) to n1, the length = n2
        # i.e calculate sum (56, 23) in case of (456, 23)
        calSum(temp, second, data)

        # now if there are nodes remaining in the list1, then add them into result
        addRestNodes(first, temp, data)
        

    if data['carry']:
        newNode = Node(data['carry'])
        newNode.next = data['result']
        data['result'] = newNode


    return data['result']
