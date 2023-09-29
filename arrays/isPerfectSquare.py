# Given a positive integer num, return true if num is a perfect square or false otherwise.

# A perfect square is an integer that is the square of an integer. In other words, it is the product of some integer with itself.

# You must not use any built-in library function, such as sqrt.

# Example 1:

# Input: num = 16
# Output: true
# Explanation: We return true because 4 * 4 = 16 and 4 is an integer.

class Solution(object):
    def     (self, num):
        """
        :type num: int
        :rtype: bool
        """
        start = 1
        end = num
        while start <= end:

            mid = (start+ end) // 2

            # print(mid)

            if mid * mid == num:
                print(mid)
                return True
            elif mid * mid < num:
                start = mid + 1
            else:
                end = mid - 1
        
        return False