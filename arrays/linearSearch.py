def linearSearch(arr,target):
    """
        linear search in an array if target is not found return -1
        Time complexity : constant - size does not matter
        Best case : 0(1) - one comparison is made.
        Worst case : 0(N) N- size of array and max comparisions made
    """

    #if array length equals zero
    if(len(arr) == 0):
        return -1


    for i in range(len(arr)):
        if(arr[i] == target):
            return i
    
    return -1

max = linearSearch([1,4,14 ,78,768],14)

print(max)