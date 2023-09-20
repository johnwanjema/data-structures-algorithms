def search2DArray(arr,target):
    """
      Search for an element in a 2d array
    """

    #if array length equals zero
    if(len(arr) == 0):
        return -1


    for i in arr:
        for j in i:
           if(j == target):
                return True
    
    return -1


print(search2DArray([{23,4,1},{18,12,3,8},{13,89}],18))