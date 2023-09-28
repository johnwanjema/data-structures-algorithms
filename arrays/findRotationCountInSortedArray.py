def countRotations(arr):
    """
      Given an array arr[] of size N having distinct numbers sorted in increasing order and the array has been right rotated (i.e, the last element will be cyclically shifted to the starting position of the array) k number of times, the task is to find the value of k.

        Examples:  

        Input: arr[] = {15, 18, 2, 3, 6, 12}
        Output: 2
        Explanation: Initial array must be {2, 3, 6, 12, 15, 18}. 
        We get the given array after rotating the initial array twice.

        Input: arr[] = {7, 9, 11, 12, 5}
        Output: 4

        Input: arr[] = {7, 9, 11, 12, 15};
        Output: 0
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

print(countRotations([4,5,6,7,0,1,2]))