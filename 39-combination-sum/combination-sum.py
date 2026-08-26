class Solution:
    def backtrack(self,idx,total,subset,nums,target,result):
        if  total==target:
            result.append(subset.copy())
            return
        elif total>target:
            return
        if idx>=len(nums):
            return
        curr_sum=total+nums[idx]
        subset.append(nums[idx])
        self.backtrack(idx,curr_sum,subset,nums,target,result)
        curr_sum=total
        subset.pop()
        self.backtrack(idx+1,curr_sum,subset,nums,target,result)
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result=[]
        self.backtrack(0,0,[],candidates,target,result)
        return result