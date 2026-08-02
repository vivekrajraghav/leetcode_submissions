# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k==0:
            return head
        length=1
        end=head
        start=head
        while end is not None and end.next is not None:
            length+=1
            end=end.next
        end.next=start
        point_to_break=length-(k%length)
        for _ in range(point_to_break):
            end=end.next
            start=start.next
        end.next=None
        return start
