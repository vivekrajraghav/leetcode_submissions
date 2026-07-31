class Solution:
    def findMin(self, nums: List[int]) -> int:
        smallest=float("inf")
        n=len(nums)
        for i in range(n):
            if nums[i]<smallest:
                smallest=min(smallest,nums[i])
        return smallest