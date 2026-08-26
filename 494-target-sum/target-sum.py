from typing import List
class Solution:
    def solve(self,idx,curr,nums,target,memo):
        if (idx,curr) in memo:
            return memo[(idx,curr)]
        if idx==len(nums):
            if curr==target:
                return 1
            return 0
        add_ways=self.solve(idx+1,curr+nums[idx],nums,target,memo)
        sub_ways=self.solve(idx+1,curr-nums[idx],nums,target,memo)
        memo[(idx,curr)]=add_ways+sub_ways
        return memo[(idx,curr)]
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo={}
        count=self.solve(0,0,nums,target,memo)
        return count