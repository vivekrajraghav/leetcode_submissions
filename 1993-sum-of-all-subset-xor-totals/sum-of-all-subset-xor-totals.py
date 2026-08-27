class Solution:
    def solve(self,idx,curr_XOR,nums):
        if idx>=len(nums):
            return curr_XOR
        include=self.solve(idx+1,curr_XOR^nums[idx],nums)
        exclude=self.solve(idx+1,curr_XOR,nums)
        return include+exclude
    def subsetXORSum(self, nums: List[int]) -> int:
        result=self.solve(0,0,nums)
        return result
