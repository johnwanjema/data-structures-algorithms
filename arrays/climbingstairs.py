def climbStairs(self, n):
    """
    You are climbing a staircase. It takes n steps to reach the top.

    Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

    Example 1:

    Input: n = 2
    Output: 2
    Explanation: There are two ways to climb to the top.
    1. 1 step + 1 step
    2. 2 steps
    """
    # Using while loop
    if(n<=3):
        return n
    n1,count = 0,0
    n2 = 1

    while count < n :
        nth = n1+n2
        n1 = n2
        n2 = nth
        count += 1
    
    return nth

    # (Recurring Condition)
    # if n <= 1: 
    #     return 1; # Case - A (Base Condition)
    # return (self.climbStairs(n - 1) + self.climbStairs(n - 2)); # Case - C 

    # Dynamic programming
    # climbStore = [0] * (n + 1)
    # climbStore[0] = 1; climbStore[1] = 1; # Base Conditions of Recursion 
    # for i in range(2, n + 1):
    #     climbStore[i] = (climbStore[i - 1] + climbStore[i - 2]) # Recurring Condition of Recursion
    # return climbStore[n] # Final Value

