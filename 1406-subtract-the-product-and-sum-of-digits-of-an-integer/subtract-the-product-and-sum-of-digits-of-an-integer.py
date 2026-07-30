class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        temp = n
        add=0
        multiply=1
        while temp>0:
            r=temp%10
            add+=r
            multiply*=r
            temp//=10
        ans=multiply-add
        return ans
        