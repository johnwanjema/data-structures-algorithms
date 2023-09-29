# Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

# You must not use any built-in exponent function or operator.

# For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
 

# Example 1:

# Input: x = 4
# Output: 2
# Explanation: The square root of 4 is 2, so we return 2.

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        l=1
        r=x
        while l<=r:
            mid = (l+r)//2
            if mid*mid == x:
                return mid
            elif mid*mid < x:
                l = mid + 1
            else:
                r = mid - 1
        
        return r
        