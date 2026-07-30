class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter=0
        max_counter=0
        n=len(nums)
        for i in range(0,n):
            if nums[i]==1:
                counter+=1
            if nums[i]!=1:
                if max_counter<counter:
                    max_counter=counter
                    counter=0
                elif max_counter>=counter:
                    counter=0
        if max_counter>counter:
            return max_counter
        else: 
            return counter

