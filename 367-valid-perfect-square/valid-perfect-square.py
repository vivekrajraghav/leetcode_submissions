class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        low=0
        high=num//2
        if num in (0,1):
            return True
        if num<0:
            return
        while high>=low:
            mid=(low+high)//2
            mid_sqr=mid*mid
            if mid_sqr==num:
                return True
            elif mid_sqr>num:
                high=mid-1
            elif mid_sqr<num:
                low=mid+1
        return False