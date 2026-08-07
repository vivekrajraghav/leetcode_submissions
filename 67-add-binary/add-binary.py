class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # i=len(a)-1
        # j=len(b)-1
        # carry=0
        # result=[]
        # while i>=0 or j>=0 or carry:
        #     total_sum=carry
        #     if i>=0:
        #         total_sum+=int(a[i])
        #         i-=1
        #     if j>=0:
        #         total_sum+=int(b[j])
        #         j-=1
        #     result.append(str(total_sum%2))
        #     carry=total_sum//2
        # return "".join(result)[::-1]
        
        # Using bit manupulation
        x=int(a,2)
        y=int(b,2)
        while y!=0:
            answer=x^y
            carry=(x&y)<<1
            x=answer
            y=carry
        return bin(x)[2:]

