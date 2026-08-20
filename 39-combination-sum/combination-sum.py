class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result=[]
        def backtrack(idx,total,subset):
            if total==target:
                result.append(subset.copy())
                return
            if total>target or idx>=len(candidates):
                return
            subset.append(candidates[idx])
            curr_sum=total+candidates[idx]
            backtrack(idx,curr_sum,subset)
            e=subset.pop()
            curr_sum-=e
            backtrack(idx+1,curr_sum,subset)
        backtrack(0,0,[])
        return result