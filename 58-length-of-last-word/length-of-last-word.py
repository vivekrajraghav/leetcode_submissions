class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=s.strip().split(" ")
        i=len(s[-1])
        return i
