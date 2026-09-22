class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        my_dict={"5":0,"10":0}
        n=len(bills)
        for i in range(n):
            if bills[i]==5:
                my_dict["5"]+=1
            elif bills[i]==10:
                if my_dict["5"]>0:
                    my_dict["10"]+=1
                    my_dict["5"]-=1
                else:
                    return False
            else:
                if my_dict["5"]>=1 and my_dict["10"]>=1:
                    my_dict["5"]-=1
                    my_dict["10"]-=1
                elif my_dict["5"]>=3:
                    my_dict["5"]-=3
                else:
                    return False
        return True