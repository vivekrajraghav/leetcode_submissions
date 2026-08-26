class Solution:
    def subset(self,idx,subpart,nums,result):
        if idx>=len(nums):
            result.append(subpart.copy())
            return
        subpart.append(nums[idx])
        self.subset(idx+1,subpart,nums,result)
        subpart.pop()
        while idx+1 <len(nums) and nums[idx]==nums[idx+1]:
            idx+=1
        self.subset(idx+1,subpart,nums,result)
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result=[]
        nums.sort()
        self.subset(0,[],nums,result)
        return result
