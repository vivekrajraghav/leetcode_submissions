class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=sorted(nums)
        longest_seq=0
        count=0
        last_element=float("-inf")
        n=len(nums)
        for i in range(0,n):
            num=nums[i]
            if num-1==last_element:
                count+=1
            elif num!=last_element:
                count=1
            last_element=num
            longest_seq=max(longest_seq,count)
        return longest_seq

