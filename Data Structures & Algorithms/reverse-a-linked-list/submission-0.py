# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def __init__(self,data=None):
            self.data=data
            self.next=None
        current=head
        prev=None
        while current is not None:
            next_node=current.next
            current.next=prev
            prev=current
            current=next_node
        return prev

            

        