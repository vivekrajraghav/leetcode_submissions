# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # if head is None:
        #     return head
        # temp=head
        # length=0
        # while temp is not None:
        #     length+=1
        #     temp=temp.next
        # if length==n:
        #     new_head=head.next
        #     return new_head
        # temp=head
        # index=length-n-1
        # for _ in range(index):
        #     temp=temp.next
        # temp.next=temp.next.next
        # return head

        # Using 2 Pointers
        if head is None:
            return head
        fast=head
        slow=head
        for _ in range(n):
            fast=fast.next
        if fast==None:
            return head.next
        while fast.next is not None:
            fast=fast.next
            slow=slow.next
        slow.next=slow.next.next
        return head