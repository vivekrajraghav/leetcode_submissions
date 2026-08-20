class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # n=len(nums)
        # total_subset=1<<n
        # result=[]
        # for num in range(total_subset):
        #     lst=[]
        #     for i in range(n):
        #         if num&(1<<i)!=0:
        #             lst.append(nums[i])
        #     result.append(lst)
        # return result

        # Using Recursion
        result=[]
        def sub_sets(idx,subset):
            if idx>=len(nums):
                result.append(subset.copy())
                return
            subset.append(nums[idx])
            sub_sets(idx+1,subset)
            subset.pop()
            sub_sets(idx+1,subset)
        sub_sets(0,[])
        return result