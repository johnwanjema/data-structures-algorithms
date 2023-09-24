# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray(object):
#    def get(self, index):
#        """
#        :type index: int
#        :rtype int
#        """
#
#    def length(self):
#        """
#        :rtype int
#        """
# Given a mountain array mountainArr,
# return the minimum index such that mountainArr.get(index) == target. If such an index does not exist,
# return -1.

# Example 1:

# Input: array = [1,2,3,4,5,3,1], target = 3
# Output: 2
# Explanation: 3 exists in the array, at index=2 and index=5. Return the minimum index, which is 2.

# Solution
# 1. Find peak element
# 2. Implement binary search twice

class Solution(object):
    def binarySearch(self,start,end,target,mountain_arr):
        isAsc = mountain_arr.get(start) < (mountain_arr.get(end))

        # print
        while start <= end:
            mid = start + (end - start ) // 2
            if(mountain_arr.get(mid) == target):
                return mid
        
            if(isAsc):
                if(target < mountain_arr.get(mid)):
                    end = mid - 1
                elif (target > mountain_arr.get(mid)):
                    start = mid + 1
            else:
                # print(isAsc)
                if(target > mountain_arr.get(mid)):
                    end = mid - 1
                elif (target < mountain_arr.get(mid)):
                    start = mid + 1

        return -1

    def findInMountainArray(self, target, mountain_arr):
        """
        :type target: integer
        :type mountain_arr: MountainArray
        :rtype: integer
        """
        l = 0
        r = mountain_arr.length()-1

        while l < r:
            mid = (l + r) // 2
            if mountain_arr.get(mid) < mountain_arr.get(mid + 1):
                l = mid + 1
            else:
                r = mid
        firstTry = self.binarySearch(0,l,target,mountain_arr)  

        if(firstTry != -1):
            return firstTry
        else:
            return self.binarySearch(l+1,mountain_arr.length()-1,target,mountain_arr)

        
        
        