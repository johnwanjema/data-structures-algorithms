def findPeakElement(arr):
    """
        finds the maximum element in an array
    """

    #if array length equals zero
    if(len(arr) == 0):
        return -1

    max = arr[0]

    for num in arr:
        if(num > max):
            max = num
    
    return max

max = findPeakElement([1, 4,4 ,78,768])

print(max)