# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # temp=head
        # my_set=set()
        # while temp is not None:
        #     if temp in my_set:
        #         return temp
        #     else:
        #         my_set.add(temp)
        #     temp=temp.next
        # return None

        # Using Slow and fast pointer to get Space(1)
        fast=head
        slow=head
        while fast is not None and fast.next is not None:
            fast=fast.next.next
            slow=slow.next
            if fast==slow:
                slow=head
                while fast!=slow:
                    fast=fast.next
                    slow=slow.next
                return fast
        return None     