# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, l_head: Optional[ListNode]) -> Optional[ListNode]:
        l_pointer = l_head
        while (l_pointer and l_pointer.next): 
            if l_pointer.val == l_pointer.next.val:
                l_pointer.next = l_pointer.next.next
            else:
                l_pointer = l_pointer.next
        
        return l_head

        