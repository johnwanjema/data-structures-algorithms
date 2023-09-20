# Binary search with ascending and descending order

def binarySearch(arr,target):
    """
       Binary search one dimensional array
    """

    #if array length equals zero
    if(len(arr) == 0):
        return -1

    # check if ascending or descending
    isAsc = arr[0] < (len(arr) - 1)
   
    
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = start + (end - start ) // 2

        if(arr[mid] == target):
            return mid
        
        if(isAsc):
            if(target < arr[mid]):
                end = mid - 1
            elif (target > arr[mid]):
                start = mid + 1
        else:
            # print(isAsc)
            if(target > arr[mid]):
                end = mid - 1
            elif (target < arr[mid]):
                start = mid + 1
    
    return -1

print(binarySearch([1,4,14,78,768],14))
print(binarySearch([111,46,40,28,6],111))