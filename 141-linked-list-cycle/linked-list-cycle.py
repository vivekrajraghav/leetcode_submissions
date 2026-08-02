# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        check=head
        my_set=set()
        while check not in my_set:
            my_set.add(check)
            if check is None:
                return False
            check=check.next
        return True
            



