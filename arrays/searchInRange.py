def linearSearch(arr,target,start,end):
    """
       Search for an element in array given the range
    """

    #if array length equals zero
    if(len(arr) == 0):
        return -1


    for i in range(start,end):
        if(arr[i] == target):
            return i
    
    return -1

max = linearSearch([18,12,-7,3,14,28],18,1,4)

print(max)