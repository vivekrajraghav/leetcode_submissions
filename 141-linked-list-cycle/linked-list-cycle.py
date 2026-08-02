# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # O(N) and Space(N)
        # check=head
        # my_set=set()
        # while check not in my_set:
        #     my_set.add(check)
        #     if check is None:
        #         return False
        #     check=check.next
        # return True
        
        # O(N) and Space(0)
        fast=head
        slow=head
        while fast is not None and fast.next is not None:
            fast=fast.next.next
            slow=slow.next
            if fast==slow:
                return True
        return False



