class Solution:
    def countRotations(self, s: str, k: int) -> int:
        n=len(s)
        if n==0:
            return 0
        c=0
        for i in range(n):
            if s[i]==s[(i+1)%n]:
                c+=1
        if k==c:
            return n-c
        elif k==c-1:
            return c
        else:
            return 0