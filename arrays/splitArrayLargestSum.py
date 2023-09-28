# Given an integer array nums and an integer k, split nums into k non-empty subarrays such that the largest sum of any subarray is minimized.

# Return the minimized largest sum of the split.

# A subarray is a contiguous part of the array.

# Example 1:

# Input: nums = [7,2,5,10,8], k = 2
# Output: 18
# Explanation: There are four ways to split nums into two subarrays.
# The best way is to split it into [7,2,5] and [10,8], where the largest sum among the two subarrays is only 18.

class Solution(object):
    def countPartitions(self, nums, maxSum):
        partitions = 1
        subSum = 0
        for num in nums:
            if subSum + num <= maxSum:
                subSum += num
            else:
                partitions += 1
                subSum = num
        return partitions

    def splitArray(self, nums, k):
        low = max(nums)
        high = sum(nums)
        while low <= high:
            mid = (low + high) // 2

            partitions = self.countPartitions(nums, mid)
            
            if partitions > k:
                low = mid + 1
            else:
                high = mid - 1
        return low