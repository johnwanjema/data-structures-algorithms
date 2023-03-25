def swapElements(arr, index1, index2):
    """
       Swaps elements in an array
    """
    temp= arr[index1]
    arr[index1] = arr[index2]
    arr[index2] = temp


def reverseArray(arr):
    """
        Reverse an array sorted in asceding order
    """

    #if array length equals zero
    if(len(arr) == 0):
        return -1

    start = 0
    end = len(arr)-1

    while(start < end):
        swapElements(arr,start,end)
        start += 1
        end -= 1

    
    
    return arr

reversedArray = reverseArray([1,4,4,7,8,7,68])

print(reversedArray)