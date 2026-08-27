class Solution:
    def solve(self,idx,subset,nums,result):
        if idx>=len(nums):
            XOR=0
            for digit in subset:
                XOR^=digit
            result.append(XOR)
            return
        subset.append(nums[idx])
        self.solve(idx+1,subset,nums,result)
        subset.pop()
        self.solve(idx+1,subset,nums,result)
    def subsetXORSum(self, nums: List[int]) -> int:
        result=[]
        self.solve(0,[],nums,result)
        return sum(result)