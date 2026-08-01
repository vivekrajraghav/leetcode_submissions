class Solution:
    def maxArea(self, height: List[int]) -> int:
        n=len(height)
        i=0
        j=n-1
        best=0
        while j>=i:
            if height[i]<=height[j]:
                temp=(height[i])*(j-i)
                best=max(best,temp)
                i+=1
            elif height[i]>=height[j]:
                temp=(height[j])*(j-i)
                best=max(best,temp)
                j-=1
        return best
                