class Solution:
    def isPalindrome(self, x: int) -> bool:
        n=len(str(x))
        rev_int=0
        if x<0:
            return False
        num=x
        for i in range(0,n):
            remainder=num%10
            rev_int=rev_int*10+remainder
            num//=10
        return rev_int==x