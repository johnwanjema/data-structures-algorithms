# Suppose you have a sorted array of infinite numbers, how would you search an element in the array?
# Source: Amazon Interview Experience. 
# Since array is sorted, the first thing clicks into mind is binary search, but the problem here is that we don’t know size of array. 
# If the array is infinite, that means we don’t have proper bounds to apply binary search. 
# So in order to find position of key, first we find bounds and then apply binary search algorithm.

# We start with a size of two then increse the bound
# 2 , 4 ,8

def infiniteArray(arr,target):
    start = 0
    end = 1

    # print(start)
    # print(end)

    while (target > arr[end]):
        temp = end + 1
        end = end + ( end - start + 1) * 2
        start = temp

        # print(start)
        # print(end)

    # return [start,end]
    return binarySearch(arr, target, start, end)
    

def binarySearch(arr,target, start, end):
    """
       Binary search one dimensional array
    """

    while start <= end:
        mid = start + (end - start ) // 2

        if(target < arr[mid]):
            end = mid - 1
        elif (target > arr[mid]):
            start = mid + 1
        else:
            return mid
    
    return -1

print(infiniteArray([3, 5, 7, 9, 10, 90, 100, 130, 140, 160, 170],10))