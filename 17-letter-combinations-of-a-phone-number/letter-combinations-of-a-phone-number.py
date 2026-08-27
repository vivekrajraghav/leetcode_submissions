class Solution:
    def solve(self,idx,subset,phone_map,digits,result):
        if idx==len(digits):
            result.append("".join(subset))
            return
        curr_digit=digits[idx]
        poss_letter=phone_map[curr_digit]
        for letter in poss_letter:
            subset.append(letter)
            self.solve(idx+1,subset,phone_map,digits,result)
            subset.pop()
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        phone_map={"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        result=[]
        self.solve(0,[],phone_map,digits,result)
        return result