class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        low=0
        high=n-1
        lb=-1
        ub=-1
        while high>=low:
            mid=(low+high)//2
            if nums[mid]==target:
                lb=mid
                high=mid-1
            elif nums[mid]>target:
                high=mid-1
            else:
                low=mid+1  
        low=0
        high=n-1
        while high>=low:
            mid=(low+high)//2
            if nums[mid]==target:
                ub=mid
                low=mid+1
            elif nums[mid]>target:
                high=mid-1
            else:
                low=mid+1
        return [lb,ub]
            