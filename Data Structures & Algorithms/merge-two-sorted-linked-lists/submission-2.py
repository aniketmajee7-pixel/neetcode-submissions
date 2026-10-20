# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head1=list1
        head2=list2
        dummy=ListNode()
        head_new=dummy
        while (head1 and head2):
            if head1.val>=head2.val:
                dummy.next=head2
                head2=head2.next
            else:
                dummy.next=head1
                head1=head1.next
            dummy=dummy.next

        if head1:
            dummy.next=head1
        elif head2:
            dummy.next=head2
            
        return head_new.next



        