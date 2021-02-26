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

array = [8, 5, 7, 2, 3]
print( findKthLargestElement(array, 2) )
