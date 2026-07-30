class Solution:
    def maxProduct(self, n: int) -> int:
        # length=len(str(n))
        # list1=[]
        # num=n
        # for i in range(length+1):
        #     remainder=num%10
        #     num//=10
        #     list1.append(remainder)
        # list1.sort()
        # max_product=list1[-1]*list1[-2]
        # return max_product

        # Better Approach
        # max1=0
        # max2=0
        # while n>0:
        #     digit=n%10
        #     n//=10
        #     if digit>max1:
        #         max2=max1
        #         max1=digit
        #     elif digit>max2:
        #         max2=digit
        # return max1*max2

        # Another approach 
        digit=sorted([int(d) for d in str(n)])
        return digit[-1]*digit[-2]