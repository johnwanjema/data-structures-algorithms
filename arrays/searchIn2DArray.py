def search2DArray(matrix,target):
    """
        Search for an element in a 2d array
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
    """

    if(len(matrix) == 0):
        return -1
    
    n=len(matrix)
    m=len(matrix[0])

    # Linear search
    for i in range(n):
        for j in range(m):
            if matrix[i][j]==target:
                return True

    return False     

print(search2DArray([[10,20,30],[15,25,35],[28,29,37]],25))