class Solution:
    def buildArray(self, nums):
        #using list comprehension
        return [nums[nums[i]] for i in range(len(nums))]