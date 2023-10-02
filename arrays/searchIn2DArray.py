def search2DArray(arr,target):
    """
        Search for an element in a 2d array
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
    """
    # n=len(matrix)
    # m=len(matrix[0])

    # Linear search
    # for i in range(n):
    #     for j in range(m):
    #         if matrix[i][j]==target:
    #             return True

    # return False     

    #if array length equals zero
    if(len(arr) == 0):
        return -1

    row = 0
    # n x m matrix
    col = len(matrix[0]) - 1
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




# print(search2DArray([[10,20,30],[15,25,35],[28,29,37]],25))
print(search2DArray([[1,3,5,7],[10,11,16,20],[23,30,34,60]],300))