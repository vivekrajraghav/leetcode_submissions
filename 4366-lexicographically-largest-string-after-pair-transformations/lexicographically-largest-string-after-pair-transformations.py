class Solution:
    def solve(self,x):
        z_value=2**25
        num_z=x//z_value
        result="z"*num_z
        remainder=x%z_value
        if remainder>0:
            binary_str=bin(remainder)[2:]
            length=len(binary_str)
            for i, bit in enumerate(binary_str):
                if bit=="1":
                    power=length-1-i
                    result+=chr(97+power)
        return result
    def largestString(self, nums: list[int]) -> list[str]:
        n=len(nums)
        final_str=[]
        for i in range(n):
            new_str=self.solve(nums[i])
            final_str.append(new_str)
        return final_str