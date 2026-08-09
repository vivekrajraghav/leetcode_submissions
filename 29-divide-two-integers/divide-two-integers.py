class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        int_max=2**31-1
        int_min=-2**31
        if dividend==int_min and divisor==-1:
            return int_max
        is_negative=(dividend<0)^(divisor<0)
        abs_dividend=abs(dividend)
        abs_divisor=abs(divisor)
        quotient=0
        for i in range(31,-1,-1):
            if (abs_divisor<<i)<=abs_dividend:
                abs_dividend-=(abs_divisor<<i)
                quotient+=(1<<i)
        if is_negative:
            quotient=-quotient
        return min(max(int_min,quotient),int_max)