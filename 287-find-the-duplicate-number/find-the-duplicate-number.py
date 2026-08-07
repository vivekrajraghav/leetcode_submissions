class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Using Floyd Hare and Tortoise Algo
        slow=0
        fast=0
        while True:
            slow=nums[slow]
            fast=nums[nums[fast]]
            if slow==fast:
                break
        slow=0
        while slow!=fast:
            slow=nums[slow]
            fast=nums[fast]
        return slow
        #Using XOR
        # n=len(nums)
        # nums.sort()
        # for i in range(1,n):
        #     if nums[i]^nums[i-1]==0:
        #         return nums[i]
        
        # Using Binary Search
        # n=len(nums)
        # low=0
        # high=n-1
        # while high>low:
        #     mid=(low+high)//2
        #     count=0
        #     for num in nums:
        #         if num<=mid:
        #             count+=1
        #     if count>mid:
        #         high=mid
        #     else:
        #         low=mid+1
        # return low
                
            