class Solution:
    def solve(self,index,flag,number,result):
        if index>=len(number):
            result.append("".join(number))
            return
        number[index]="1"
        self.solve(index+1,True,number,result)
        if flag==True:
            number[index]="0"
            self.solve(index+1,False,number,result)
            number[index]="1"
    def validStrings(self, n: int) -> List[:str]:
        number=["1"]*n
        result=[]
        self.solve(0,True,number,result)
        return result