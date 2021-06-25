'''
    Idea is, we will iterate over every element and also maintain the increasingSeq array, if the
    current element is greater than last element of increasingSeq then simply append in it, if current
    element is smaller than last element, then find its correct position (by finding its ceil) using binary search.
'''
def longestIncreasingSubsequence(array):
    increasingSeq = [ array[0] ]

    for i in range(1, len(array)):
        current = array[i]

        if current >= increasingSeq[-1]:
            increasingSeq.append( current )
        else:
            start = 0
            end = len(increasingSeq) - 1
            ceil = -1
            
            while start <= end:
                mid = start + (end - start) // 2

                if current == increasingSeq[mid]:
                    ceil = mid
                    break
                elif current < increasingSeq[mid]:
                    ceil = mid
                    end = mid - 1
                else:
                    start = mid + 1

            increasingSeq[ ceil ] = current

    return increasingSeq
