def CeillingOfANumber(arr,target):
    """
       Ceilling of a number is a number greater than or equal to target element
    """
    print(target)
    print(arr)
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

  
    return arr[start]

print(CeillingOfANumber([2,3,5,9,14,16,18],15))