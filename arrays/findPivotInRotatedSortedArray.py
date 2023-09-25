def findPivotInRotatedSortedArray(arr,target):
    """
       Binary search one dimensional array
    """

    #if array length equals zero
    if(len(arr) == 0):
        return -1

    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = start + (end - start ) // 2

        if(target < arr[mid]):
            end = mid - 1
        elif (target > arr[mid]):
            start = mid + 1
        else:
            return mid
    
    return -1

print(findPivotInRotatedSortedArray([1,4,14 ,78,768],14))