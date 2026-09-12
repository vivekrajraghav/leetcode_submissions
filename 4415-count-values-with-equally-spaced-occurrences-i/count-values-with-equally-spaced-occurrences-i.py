from collections import Counter
class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        index_map=defaultdict(list)
        for i, val in enumerate(nums):
            index_map[val].append(i)
        counter=0
        for idx in index_map.values():
            if len(idx)==3:
                gap=idx[1]-idx[0]
                if idx[2]-idx[1]==gap:
                    counter+=1
        return counter
        