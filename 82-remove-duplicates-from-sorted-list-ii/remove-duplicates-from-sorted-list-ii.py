# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        dummy=ListNode(0,head)
        back=dummy
        front=head
        while front:
            if front.next and front.val==front.next.val:
                while front.next and front.val==front.next.val:
                    front=front.next
                back.next=front.next
            else:
                back=back.next
            front=front.next
        return dummy.next