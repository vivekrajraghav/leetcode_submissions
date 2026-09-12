class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        index_map=defaultdict(list)
        for i , val in enumerate(nums):
            index_map[val].append(i)
        counter=0
        for idx in index_map.values():
            if len(idx)>=3:
                gap=idx[1]-idx[0]
                is_equal=all(idx[i]-idx[i-1]==gap for i in range(2,len(idx)))
                if is_equal:
                    counter+=1
        return counter