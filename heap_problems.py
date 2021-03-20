
import heapq as heap
import math

'''
    Idea is: store the first k element in the min heap, and when traversing from (k + 1) to n
    pop one element from heap if root of heap is less than current element and insert new element in heap 
'''
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

def findKClosestToX(arr, k, X):
    maxHeap = []
    for i in range(k):
        diff = abs(arr[i] - X)
        # using the difference as the key, inorder to maintain the heap and value as the element
        # as internally, heapq creates minHeap, therefore multiplying distance with -1
        heap.heappush(maxHeap, [-diff, arr[i]])

    # [-2, 5], [-1, 6], [0, 7]
    for i in range(k, len(arr)):
        num = arr[i]
        diff = abs(num - X)

        if diff < (-1 * maxHeap[0][0]):
            pop = heap.heappop(maxHeap)
            heap.heappush(maxHeap, [-diff, arr[i]])

    print(maxHeap)

'''
    k sorted array means, each element at index i will have it's position in range of (i - k) to
    (i + k) in sorted array. we can simply use some sorting algorithm on entire array and achieve
    sorted array in O(nlogn) time, but we can do it in O(nlogk) since we know array is k-sorted.

    Idea is, first we will store (k + 1) elements in minHeap, when k+1 element will occur, we will pop min element
    and append it to the ans, and insert k+1 element in minheap
'''
def kSortedArray(arr, k):
    minHeap = []
    ans = []
    for i in range(k + 1):
        heap.heappush(minHeap, arr[i])

    # After this loop we will have (n - k) elements in ans
    for i in range(k + 1, len(arr)):
        ans.append( heap.heappop(minHeap) )
        heap.heappush(minHeap, arr[i])

    # Now inserting remaining elements in ans
    while len(minHeap):
        ans.append( heap.heappop(minHeap) )

    print(ans)

'''
    For this the naive approach could be, store all the element-count pair in dictionary, and then sort if using
    value as key, this could result in O(dlogd) where d = number of distinct elements.
    But we can use heap, store all the [count, element] pair in it, key will be the count of element,
    and then pop the top k elements, it will result in O(klogd + d), as To remove the top of heap O(log d)
    time is required, so if k elements are removed then O(k log d) time is required and
    to traverse the distinct elements O(d) time is required.
'''
def topKFrequentElements(arr, k):
    elementToCount = {}
    for num in arr:
        if num not in elementToCount:
            elementToCount[num] = 1
        else:
            elementToCount[num] += 1

    if k > len(elementToCount):
        print("Invalid input")
    else:
        maxHeap = [(value, key) for key, value in elementToCount.items()]

        largest = heap.nlargest(k, maxHeap)
 
        # Print the top k elements
        for i in range(k):
            print(largest[i][1], end =" ")


def kClosestPointToOrigin(coords, k):
    '''
        coords: array of [x, y] co-oridnates, k:integer
        First creating (distance, coord) pair, and then storing all pairs in heap, this will take O(n) time
        Then we are taking smallest k pair, for each pair it will take O(logn) time and we are doing it for
        k times, therefore it will take O(klogn), therefore total time will be O(n + klogn)
    '''
    # Storing (distance, coord) pairs to minHeap
    minHeap = [ ( math.sqrt(x**2 + y**2), [x, y] ) for (x, y) in coords]
    ksmallest = heap.nsmallest(k, minHeap)

    for distance, coord in ksmallest:
        print(distance, coord)


'''
    Idea is: since we have to keep the array sorted as the element comes, but since we only care about only
    middle elements in sorted array, therefore we will create two heaps, max heap for first half of sorted array
    and min heap for next half of sorted array, at any time if they becomes imbalanced, then we will rebalanced them.
    if there len are same, (i.e total number of elements are even) thenwe will take the average of root of both heaps,
    else we will take root from that heap which contains more number of elements.
'''

def continousMedian(array):
    maxHeap = []
    minHeap = []
    medians = []
    
    for num in array:
        # if maxHeap is empty or current element is smaller than root of maxheap
        # as bydefault, internally min heap is created so using -ve everywhere in order to make it maxheap
        if len(maxHeap) == 0 or num < (-1*maxHeap[0]):
            heap.heappush( maxHeap, -num )
        else:
            heap.heappush( minHeap, num )


        # now checking for imbalanced, at any time if lefthalf and right half differes by 2
        if len(maxHeap) - len(minHeap) == 2:
            pop = heap.heappop( maxHeap )
            heap.heappush( minHeap, pop )
        # if right half - lefthalf differs by 2
        elif len(minHeap) - len( maxHeap ) == 2:
            pop = heap.heappop( minHeap )
            heap.heappush( maxHeap, -pop )

        # Now the heaps are balanced, we just need to calculate median
        if len(minHeap) == len(maxHeap):
            median = ( minHeap[0] + (-maxHeap[0]) ) / 2
        else:
            # i.e total number of elements are odd
            if len(minHeap) > len(maxHeap):
                median = minHeap[0]
            else:
                median = -maxHeap[0]
                
        medians.append(median)
        
    return medians

        
array = [8, 5, 7, 2, 3]
print( findKthLargestElement(array, 2) )


print( minCostToConnectRopes(array) )


arr = [5, 6, 7, 8, 9]
findKClosestToX(arr, 3, 7)


kSortedArr = [6, 5, 3, 2, 8, 10, 9]
kSortedArray(kSortedArr, 3)



arr = [ 3, 1, 4, 4, 5, 2, 6, 1 ]
k = 2
topKFrequentElements(arr, k)


coords = [ [1, 2], [-1, 4], [3, 4], [1, 0], [5, -2] ]
k = 2
kClosestPointToOrigin(coords, k)


array = [5, 10, 100, 200, 6, 13, 14]
print( continousMedian(array) )
