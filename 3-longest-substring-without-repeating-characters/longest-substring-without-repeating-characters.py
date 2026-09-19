class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        maxi=0
        n=len(s)
        for i in range(0,n):
            my_set=set()
            for j in range(i,n):
                if s[j] in my_set:
                    break
                maxi=max(maxi,j-i+1)
                my_set.add(s[j])
        return maxi