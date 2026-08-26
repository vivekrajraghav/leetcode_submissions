class Solution:
    def backtrack(self,subset,idx,target,result,candidates):
        if target==0:
            result.append(subset.copy())
            return
        elif target<0:
            return
        if idx>=len(candidates):
            return
        for i in range(idx,len(candidates)):
            if i>idx and candidates[i]==candidates[i-1]:
                continue
            if candidates[i]>target:
                break
            subset.append(candidates[i])
            self.backtrack(subset,i+1,target-candidates[i],result,candidates)
            subset.pop()
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result=[]
        candidates.sort()
        self.backtrack([],0,target,result,candidates)
        return result