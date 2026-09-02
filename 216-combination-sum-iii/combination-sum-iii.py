class Solution:
    def solve(self,last,total,subset,result,k,n):
        if total==n and len(subset)==k:
            result.append(subset.copy())
            return
        if total>n or len(subset)>k:
            return
        for i in range(last,10):
            curr_sum=total+i
            subset.append(i)
            self.solve(i+1,curr_sum,subset,result,k,n)
            subset.pop()
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result=[]
        self.solve(1,0,[],result,k,n)
        return result