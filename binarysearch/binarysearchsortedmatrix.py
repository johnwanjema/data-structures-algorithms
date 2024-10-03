# Time complexity O( log n + log m)
class Solution:
    def searchSortedMatrix(self, matrix, target: int) -> bool:
        # Get the number of rows in the matrix
        rows = len(matrix)
        
        # Ensure the matrix has columns (matrix may be empty)
        if len(matrix[0]) != 0:
            cols = len(matrix[0]) # Number of columns
        
        # If the matrix has only one row, perform binary search on that row
        if rows == 1:
            return self.binarysearch(matrix, 0, 0, cols - 1, target)

        # Initialize row start and row end indices
        rstart = 0
        rEnd = rows - 1
        # Find the middle column to focus on for binary search
        midCol = cols // 2

        # Run the loop until two rows remain
        # This loop helps reduce the search space to two rows
        while rstart < rEnd - 1:
            # Calculate the mid row for dividing the matrix
            midrow = rstart + (rEnd - rstart) // 2

            # Check if the target is in the middle column of the mid row
            if matrix[midrow][midCol] == target:
                return [midrow, midCol]
            # If target is smaller than the mid column value, search in upper half
            if matrix[midrow][midCol] > target:
                rEnd = midrow 
            # If target is larger, search in the lower half
            else:
                rstart = midrow

        # After the loop, two rows remain (rstart and rstart + 1)
        # Check if the target is in the mid column of these rows
        if matrix[rstart][midCol] == target:
            return [rstart, midCol]
        
        if matrix[rstart + 1][midCol] == target:
            return [rstart + 1, midCol]
        
        # Search in the first half (left of midCol) of the first remaining row
        if target <= matrix[rstart][midCol - 1]:
            print(matrix[rstart][midCol])
            return self.binarysearch(matrix, rstart, 0, midCol - 1, target)
        
        # Search in the second half (right of midCol) of the first remaining row
        if target >= matrix[rstart][midCol + 1] and target <= matrix[rstart][cols - 1]:
            return self.binarysearch(matrix, rstart, midCol + 1, cols - 1, target)
        
        # Search in the first half (left of midCol) of the second remaining row
        if target <= matrix[rstart + 1][midCol - 1]:
            return self.binarysearch(matrix, rstart + 1, 0, midCol - 1, target)
        
        # Search in the second half (right of midCol) of the second remaining row
        else:
            return self.binarysearch(matrix, rstart + 1, midCol + 1, cols - 1, target)

    # Binary search helper function
    # Searches in the specified row between colstart and colend for the target
    def binarysearch(self, arr, row, colstart, colend, target):
        while colstart <= colend:
            # Find the mid point in the column range
            mid = colstart + (colend - colstart) // 2

            # If target is found, return its position
            if arr[row][mid] == target:
                return [row, mid]
            
            # If mid element is greater than target, move left
            if arr[row][mid] > target:
                colend = mid - 1
            # If mid element is smaller than target, move right
            else:
                colstart = mid + 1

        # If not found, return [-1, -1] to indicate failure
        return [-1, -1]
    
# Example usage
sol = Solution()

mat = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
      ]
      
print(sol.searchSortedMatrix(mat, 12))
