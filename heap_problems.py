'''
    Idea is: store the first k element in the min heap, and when traversing from (k + 1) to n
    pop one element from heap if root of heap is less than current element and insert new element in heap 
'''
import heapq as heap

def findKthLargestElement(array, k):
    minHeap = []
    # inserting first k elements in heap
    for i in range(k):
        heap.heappush(minHeap, array[i])

    for i in range(k, len(array)):
        # as root is smallest element
        if minHeap[0] < array[i]:
            poppedElement = heap.heappop(minHeap)
            heap.heappush(minHeap, array[i])
            
    return minHeap[-k]

# Given an array, where each element represents the length of rope, task is to connect all the ropes but with min cost
# Cost is defined as sum of two ropes which are getting connected
# Idea is, use min heap, first put all the elements in it, then always pop 2 min elements (ropes) and calculate cost.
# Then put the resultant rope again in the heap

def minCostToConnectRopes(array):
    minHeap = []
    for num in array:
        heap.heappush( minHeap, num )

    overAllCost = 0
    # while there is only one role in the heap
    while len(minHeap) != 1:
        first = heap.heappop(minHeap)
        second = heap.heappop(minHeap)

        intermediateCost = first + second
        overAllCost += intermediateCost

        heap.heappush(minHeap, intermediateCost)
        
    return overAllCost

array = [8, 5, 7, 2, 3]
print( findKthLargestElement(array, 2) )

print( minCostToConnectRopes(array) )
