class Solution:
    def solve(self,index,total,brackets,result):
        if len(brackets)==index:
            if total==0:
                result.append("".join(brackets))
            return
        if total<0:
            return
        if total>len(brackets)//2:
            return
        brackets[index]="("
        self.solve(index+1,total+1,brackets,result)
        brackets[index]=")"
        self.solve(index+1,total-1,brackets,result)
    def generateParenthesis(self, n: int) -> List[str]:
        result=[]
        brackets=[""]*(2*n)
        self.solve(0,0,brackets,result)
        return result