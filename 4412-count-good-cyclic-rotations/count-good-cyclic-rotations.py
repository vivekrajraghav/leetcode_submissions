class Solution:
    def countGoodRotations(self, nums: list[int]) -> int:
        n=len(nums)
        half=n//2
        total=sum(nums)
        first_half=sum(nums[:half])
        count=0
        for i in range(n):
            if 2*first_half>total:
                count+=1
            first_half-=nums[i]
            first_half+=nums[(i+half)%n]
        return count