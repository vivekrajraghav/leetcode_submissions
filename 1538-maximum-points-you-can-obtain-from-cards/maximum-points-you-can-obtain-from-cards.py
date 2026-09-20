class Solution:
    def maxScore(self, cardPoints: list[int], k: int) -> int:
        left_sum=0
        right_sum=0
        overall=0
        n=len(cardPoints)
        for i in range(0,k):
            left_sum+=cardPoints[i]
        overall=left_sum
        right_idx=n-1
        for i in range(k-1,-1,-1):
            left_sum-=cardPoints[i]
            right_sum+=cardPoints[right_idx]
            overall=max(overall,right_sum+left_sum)
            right_idx-=1
        return overall
