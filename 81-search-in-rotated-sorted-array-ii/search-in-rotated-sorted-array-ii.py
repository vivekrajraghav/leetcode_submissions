class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        nums.sort()
        n=len(nums)
        low=0
        high=n-1
        while high>=low:
            mid=(low+high)//2
            mid_value=nums[mid]
            if mid_value==target:
                return True
            elif mid_value>target:
                high=mid-1
            elif mid_value<target:
                low=mid+1
        return False