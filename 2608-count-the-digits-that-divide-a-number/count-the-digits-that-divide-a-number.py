class Solution:
    def countDigits(self, num: int) -> int:
        counter=0
        n=len(str(num))
        digit=num
        if num<=10:
            return 1
        for i in range(n+1):
            divider=digit%10
            digit//=10
            if divider!=0 and num%divider==0:
                counter+=1
        return counter