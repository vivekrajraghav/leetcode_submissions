class Solution:
    def mySqrt(self, x: int) -> int:
        if x in (0,1):
            return x
        if x<0:
            return
        low=0
        high=x//2
        ans=0
        while high>=low:
            mid=(low+high)//2
            mid_sqr=mid*mid
            if mid_sqr==x:
                return  mid
            elif mid_sqr>x:
                high=mid-1
            elif mid_sqr<x:
                low=mid+1
                ans=mid 
        return int(ans)