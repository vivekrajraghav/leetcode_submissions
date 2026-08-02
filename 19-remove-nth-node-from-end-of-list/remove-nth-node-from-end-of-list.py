# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return head
        temp=head
        length=0
        while temp is not None:
            length+=1
            temp=temp.next
        if length==n:
            new_head=head.next
            return new_head
        temp=head
        index=length-n-1
        for _ in range(index):
            temp=temp.next
        temp.next=temp.next.next
        return head