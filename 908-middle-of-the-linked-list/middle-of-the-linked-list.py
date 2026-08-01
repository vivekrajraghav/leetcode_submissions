# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # O(N)
        # curr=head
        # count=0
        # while curr is not None:
        #     count+=1
        #     curr=curr.next
        # curr=head
        # for _ in range(count//2):
        #     curr=curr.next
        # return curr

        # O(N/2)
        fast=head
        slow=head
        while fast is not None and fast.next is not None:
            slow=slow.next
            fast=fast.next.next
        return slow