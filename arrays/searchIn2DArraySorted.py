def search2DArraSorted(matrix,target):
    """
        Search for an element in a 2d array
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
    """

    #if array length equals zero
    if(len(matrix) == 0):
        return -1

    row = 0
    # n x m matrix
    # col = len(matrix[0]) - 1

    # n x n matrix
    col = len(matrix) - 1

    while row < len(matrix) and col >= 0:
        if(matrix[row][col] == target):
            return True
        
        if(matrix[row][col] < target):
            row += 1
        else:
            col -= 1
    
    return False  

print(search2DArraSorted([[1,3,5,7],[10,11,16,20],[23,30,34,60]],30))