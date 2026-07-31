class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # nums.sort()
        # n=len(nums)
        # low=0
        # high=n-1
        # while high>=low:
        #     mid=(low+high)//2
        #     mid_value=nums[mid]
        #     if mid_value==target:
        #         return True
        #     elif mid_value>target:
        #         high=mid-1
        #     elif mid_value<target:
        #         low=mid+1
        # return False

        # Without .sort()
        n=len(nums)
        low=0
        high=n-1
        while high>=low:
            mid=(low+high)//2
            if nums[mid]==target:
                return True
            if nums[mid]==nums[low]==nums[high]:
                low+=1
                high-=1
                continue
            if nums[low]<=nums[mid]: # If left part is stoted
                if nums[low]<=target<nums[mid]:
                    high=mid-1
                else:
                    low=mid+1
            else: # IF right part is sorted
                if nums[mid]<target<=nums[high]:
                    low=mid+1
                else:
                    high=mid-1
        return False
            