class Solution:
    def isPowerOfThree(self, n: int) -> bool:
# Solving through Loop
        # if n<=0:
        #     return False
        # while n%3==0:
        #     n=n//3
        # return n==1
# Using Recursion
        if n<=0:
            return False
        if n==1:
            return True
        if n%3==0:
            return self.isPowerOfThree(n//3)
        return n==1
            