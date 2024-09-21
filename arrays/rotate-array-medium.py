def rotate(nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        # Brute force
        # for i in range(k):
        #     print(i)
        #     temp = nums[-1]
        #     for i in range(len(nums)-1,-1,-1):
        #         nums[i] = nums[i-1]
        #     nums[0] = temp   
        
        if k > len(nums):
            k = k - len(nums)
        i = len(nums) - k
        nums[:] = nums[i:] + nums[:i]