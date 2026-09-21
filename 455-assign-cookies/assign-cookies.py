class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        g.sort(reverse=True)
        s.sort(reverse=True)
        sidx=0
        count=0
        n=len(g)
        for i in range(n):
            if sidx>=len(s):
                return count
            if g[i]<=s[sidx]:
                count+=1
                sidx+=1
        return count
