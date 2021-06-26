'''
    Idea is, we will use the concept of peeks and valleys, whenever we found valley we will start
    expnading towards it's left and right, if we are heading to the peek, then continously increase
    reward.
'''

def minRewards(array):
    n = len(array)

    # setting the initial reward as 1 for all students
    rewards = [1] * n 
    for i in range(1, n-1):
        # if we found the valley
        if (array[i] < array[i-1]) and (array[i] < array[i+1]):
            expand(i, array, rewards)

    return rewards

def expand(i, array, rewards):
    leftIdx = i-1

    while leftIdx >= 0 and array[leftIdx] > array[leftIdx+1]:
        rewards[leftIdx] = max( rewards[leftIdx], rewards[leftIdx+1] + 1 )
        leftIdx -= 1

    rightIdx = i+1
    while rightIdx < len(array) and array[rightIdx] > array[rightIdx-1]:
        rewards[rightIdx] = max( rewards[rightIdx], rewards[rightIdx-1] + 1 )
        rightIdx += 1
