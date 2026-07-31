class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n=len(word1)
        m=len(word2)
        looping=min(n,m)
        i=0
        j=0
        result=""
        for k in range(looping):
            result+=word1[i]
            i+=1
            result+=word2[j]
            j+=1
        while n>i:
            result+=word1[i]
            i+=1
        while m>j:
            result+=word2[j]
            j+=1
        return result