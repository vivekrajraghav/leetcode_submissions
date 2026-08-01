class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #Using Bubble Sort
        # n=len(nums)
        # for i in range(n-2,-1,-1):
        #    for j in range(0,i+1):
        #     if nums[j]>nums[j+1]:
        #         nums[j],nums[j+1]=nums[j+1],nums[j]
        
        # Dutch National Flag Algo
        n=len(nums)
        start=0
        mid=0
        end=n-1
        while end>=mid:
            if nums[mid]==0:
                nums[mid],nums[start]=nums[start],nums[mid]
                start+=1
                mid+=1
            elif nums[mid]==1:
                mid+=1
            else:
                nums[mid],nums[end]=nums[end],nums[mid]
                end-=1