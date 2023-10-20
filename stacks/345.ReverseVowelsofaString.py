# Given a string s, reverse only all the vowels in the string and return it.

# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

# Example 1:

# Input: s = "hello"
# Output: "holle"
# Example 2:

# Input: s = "leetcode"
# Output: "leotcede"

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Stack is LIFO last in First out
        stack = []
        res = ""
        for i in s:
            if i in 'aeiouAEIOU':
                stack.append(i)

       
        for char in s:
            if char in 'aeiouAEIOU':              
                res+=stack.pop()            
            else:
                res+=char   

        return res