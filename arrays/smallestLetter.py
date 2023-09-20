#  Find the smallest letter greater than target
#  You are given an array of characters letters that is sorted in non-decreasing order, and a character target. There are at least two different characters in letters.

# Return the smallest character in letters that is lexicographically greater than target. If such a character does not exist, return the first character in letters.

 

# Example 1:

# Input: letters = ["c","f","j"], target = "a"
# Output: "c"
# Explanation: The smallest character that is lexicographically greater than 'a' in letters is 'c'.


# class Solution(object):
def nextGreatestLetter(letters, target):
    """
    :type letters: List[str]
    :type target: str
    :rtype: str
    """
    start = 0
    end = len(letters)-1

    while start <= end:
        mid = start + (end - start) // 2

        if target < letters[mid]:
            end = mid - 1
        else:
            start = mid + 1

    return letters[start % len(letters)]

print(nextGreatestLetter(["c","f","j"],"a"))
    

