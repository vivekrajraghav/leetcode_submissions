class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive_arr=[]
        negative_arr=[]
        for i in range(0,len(nums)):
            if nums[i]>0:
                positive_arr.append(nums[i])
            if nums[i]<0:
                negative_arr.append(nums[i])
        new_list=[]
        for i in range(0,len(positive_arr)):
            new_list.append(positive_arr[i])
            new_list.append(negative_arr[i])
        return new_list