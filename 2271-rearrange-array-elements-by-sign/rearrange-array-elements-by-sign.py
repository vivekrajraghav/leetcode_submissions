class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
    #   Brute Force Approach
        # positive_arr=[]
        # negative_arr=[]
        # for i in range(0,len(nums)):
        #     if nums[i]>0:
        #         positive_arr.append(nums[i])
        #     if nums[i]<0:
        #         negative_arr.append(nums[i])
        # new_list=[]
        # for i in range(0,len(positive_arr)):
        #     new_list.append(positive_arr[i])
        #     new_list.append(negative_arr[i])
        # return new_list

        # Better approach
        n=len(nums)
        result=[0]*n
        i=0
        j=1
        for k in range(0,n):
            if nums[k]>0:
                result[i]=nums[k]
                i+=2
            if nums[k]<0:
                result[j]=nums[k]
                j+=2
        return result