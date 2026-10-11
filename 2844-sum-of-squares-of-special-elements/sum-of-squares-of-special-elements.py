class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        result=0
        n=len(nums)
        for i in range(n):
            if n%(i+1)==0:
                sum_square=nums[i]**2
                result+=sum_square
        return result