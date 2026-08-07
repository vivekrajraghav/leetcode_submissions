class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        while b!=0:
            answer=(a^b)&mask
            carry=((a&b)<<1)&mask
            a=answer
            b=carry
        max_int=0x7FFFFFFF
        if a<=max_int:
            return a
        else:
            return ~(a^mask)