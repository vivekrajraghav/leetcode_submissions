class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        ans=0
        limit=min(a,b)
        for i in range(1,limit+1):
            if a%i==0 and b%i==0:
                ans+=1
        return ans
        