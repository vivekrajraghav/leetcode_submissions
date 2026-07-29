class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Time complexity of O(NlogN)
        # n=len(nums)
        # check=0
        # nums.sort()
        # for i in range(0,n):
        #     if check==nums[i]:
        #         check+=1
        #     elif check!=nums[i]:
        #         return check
        # return check
        # Better Approach using XOR operator Time complexity O(N)
        result=len(nums)
        for i,num in enumerate(nums):
            result=result^i^num
        return result
