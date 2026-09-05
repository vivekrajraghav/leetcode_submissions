class Solution:
    # def solve(self,i,haystack,needle,word_idx):
    #     if word_idx>=len(needle):
    #         return i-word_idx
    #     if i>=len(haystack):
    #         return -1
    #     if haystack[i]!=needle[word_idx]:
    #         return -1
    #     return self.solve(i+1,haystack,needle,word_idx+1)
    # def strStr(self, haystack: str, needle: str) -> int:
    #     for i in range(len(haystack)):
    #         if haystack[i]==needle[0]:
    #             ans=self.solve(i,haystack,needle,0)
    #             if ans>=0:
    #                 return i
    #     return -1

    def strStr(self, haystack: str, needle: str) -> int:
        n=len(needle)
        for i in range(len(haystack)-n+1):
            if haystack[i:i+n]==needle:
                return i
        return -1