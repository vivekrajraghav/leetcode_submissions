class Solution:
    def smallestNumber(self, n: int) -> int:
        # push=n.bit_length()
        # largest=2**31-1
        # new_num=largest>>(31-push)
        # return new_num

        # More consize and better
        return (1<<n.bit_length())-1