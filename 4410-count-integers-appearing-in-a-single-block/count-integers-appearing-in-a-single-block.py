class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        seen=set()
        invalid=set()
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            if nums[i] in seen:
                invalid.add(nums[i])
            else:
                seen.add(nums[i])
        return len(seen)-len(invalid)