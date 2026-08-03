# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        front=head
        while front:
            if front.next and front.val==front.next.val:
                front.next=front.next.next
            else:
                front=front.next
        return head
