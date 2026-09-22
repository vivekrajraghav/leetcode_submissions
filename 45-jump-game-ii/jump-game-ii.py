class Solution:
    def jump(self, nums: list[int]) -> int:
        n=len(nums)
        left=0
        right=0
        jump=0
        farthest=0
        while right<n-1:
            for i in range(left,right+1):
                farthest=max(farthest,nums[i]+i)
            left=right+1
            right=farthest
            jump+=1
        return jump