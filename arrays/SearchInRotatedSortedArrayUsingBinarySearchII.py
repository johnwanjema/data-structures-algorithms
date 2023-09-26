# There is an integer array nums sorted in ascending order (with distinct values).

# Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

# Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4


# Code for sorted array with duplicate values
class Solution(object):
    def binarySearch(self,start,end, arr,target):
        while start <= end:
            mid = start + (end - start ) // 2
            print(target)
            print(arr[mid])
            if(target == arr[mid]):
                return mid
            elif(target < arr[mid]):
                end = mid - 1
            elif (target > arr[mid]):
                start = mid + 1
    
        return -1

    def findPivot(self,nums):
        # Find Pivot
        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = start + (end - start ) // 2

            if(mid < end and nums[mid] > nums[mid+1]):
               return mid
            if( mid > start and nums[mid] < nums[mid-1]):
                return mid
            if(nums[start] >= nums[mid-1]):
                end = mid - 1
            else:
                start = mid + 1

        return -1

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        pivot = self.findPivot(nums)

        # If there is no pivot array is not rotated
        if pivot == -1:
            return self.binarySearch(0,len(nums) - 1,nums,target)

        if nums[pivot] == target:
            return pivot

        if target >= nums[0]:
            return self.binarySearch(0,pivot-1,nums,target)
        
        return self.binarySearch(pivot+1,len(nums) - 1,nums,target)
        