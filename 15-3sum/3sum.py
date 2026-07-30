class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result=set()
        nums.sort()
        n=len(nums)
        for i in range(0,n):
            if i!=0 and nums[i]==nums[i-1]:
                continue
            j=i+1
            k=n-1
            while k>j:
                total_sum=nums[i]+nums[j]+nums[k]
                if total_sum==0:
                    result.add(tuple([nums[i],nums[j],nums[k]]))
                    j+=1
                    k-=1
                elif total_sum<0:
                    j+=1
                elif total_sum>0:
                    k-=1
        return [list(ans) for ans in result]