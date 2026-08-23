class Solution:
    def isPalindromic(self, s: str) -> bool:
        new_list=[]
        for ch in s:
            temp=bin(ord(ch))
            new_list.append(temp[2:].zfill(8))
        new_str="".join(new_list)
        rev_str=new_str[::-1]
        return new_str==rev_str