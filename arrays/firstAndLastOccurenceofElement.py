# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

# If target is not found in the array, return [-1, -1].

# You must write an algorithm with O(log n) runtime complexity.

# Example 1:
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Example 2:

# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ans = [-1,-1]

        def binarySearch(nums,target, findFirstIndex):
            start = 0
            end = len(nums) - 1
            ans = -1

            while start <= end:
                mid = start + (end - start) // 2
                if(nums[mid] == target):
                    ans = mid
                    if(findFirstIndex):
                        end = mid -1
                    else:
                        start = mid + 1
                elif target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            return ans

        ans[0] = binarySearch(nums,target,True)
        ans[1] = binarySearch(nums,target,False)
    
        return ans
