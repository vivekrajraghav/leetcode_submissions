class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Time complexity of O(nlogn)
        # nums=sorted(nums)
        # longest_seq=0
        # count=0
        # last_element=float("-inf")
        # n=len(nums)
        # for i in range(0,n):
        #     num=nums[i]
        #     if num-1==last_element:
        #         count+=1
        #     elif num!=last_element:
        #         count=1
        #     last_element=num
        #     longest_seq=max(longest_seq,count)
        # return longest_seq

        # Optimal Solution O(n)
        my_set=set(nums)
        longest_seq=0
        for num in my_set:
            if (num-1) not in my_set:
                current_num=num
                count=1
                while current_num+1 in my_set:
                    current_num+=1
                    count+=1
                longest_seq=max(longest_seq,count)
        return longest_seq