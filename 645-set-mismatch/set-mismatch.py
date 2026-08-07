class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n=len(nums)
        for i in range(n):
            while nums[i]!=nums[nums[i]-1]:
                swap_idx=nums[i]-1
                nums[i],nums[swap_idx]=nums[swap_idx],nums[i]
        for i in range(n):
            if nums[i]!=i+1:
                return [nums[i],i+1]
                    