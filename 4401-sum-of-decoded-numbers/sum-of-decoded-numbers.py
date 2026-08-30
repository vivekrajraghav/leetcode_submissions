class Solution:
    def solve(self,x,MOD):
        width=x%10
        di=str(x//10)
        xi=int(di[:width])
        yi=int(di[width:])
        return pow(xi,yi,MOD)
    def sumDecoded(self, nums: list[int]) -> int:
        n=len(nums)
        result=0
        MOD=10**9+7
        for i in range(n):
            result=(result+self.solve(nums[i],MOD))%MOD
        return result