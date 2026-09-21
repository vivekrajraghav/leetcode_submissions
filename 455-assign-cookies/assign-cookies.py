class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        n=len(g)
        m=len(s)
        count=0
        i,j=0,0
        g.sort()
        s.sort()
        while i<n and j<m:
            if g[i]<=s[j]:
                count+=1
                i+=1
            j+=1
        return count