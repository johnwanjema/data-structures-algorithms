def smallerNumbersThanCurrent(nums):
        retval = []
        for num in nums:
            count = 0
            for x in nums:
                if num > x:
                    count += 1
            retval.append(count)
        
        return retval

# Time complexity o(n^2)