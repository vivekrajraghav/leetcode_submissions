class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
    #     n=len(digits)
    #     string=[]
    #     for i in range(0,n):
    #         string.append(str(digits[i]))
    #     string="".join(string)
    #     string=str((int(string)+1))
    #     result=[int(char) for char in string]
    #     return result

    # Another approach
        for i in range(len(digits)-1,-1,-1):
            if digits[i]==9:
                digits[i]=0
            else:
                digits[i]+=1
                return digits
        return [1]+digits