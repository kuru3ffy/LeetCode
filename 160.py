# Definition for singly-linked list.
#class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if headA == None or headB == None:
            return None

        LNA = headA
        LNB = headB
        while LNA != LNB:
            LNA = headB if LNA == None else LNA.next
            LNB = headA if LNB == None else LNB.next
        return LNA