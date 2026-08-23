class Solution:
    def findDisappearedNumbers(self, nums: list[int], lower: int, upper: int) -> list[list[int]]:
        nums.sort()
        result=[]
        curr=lower
        for num in nums:
            if curr>num:
                continue
            if num==curr:
                curr+=1
            elif num>curr:
                result.append([curr,min(num-1,upper)])
                curr=num+1
            if curr>upper:
                break
        if curr<=upper:
            result.append([curr,upper])
        return result