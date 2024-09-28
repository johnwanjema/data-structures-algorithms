class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        rows = 0
        cols = len(matrix[0]) - 1

        while rows < len(matrix) and cols >= 0:
            if(matrix[rows][cols] == target):
                return 1
            elif matrix[rows][cols] < target:
                rows += 1
            else:
                cols -= 1
        
        return 0