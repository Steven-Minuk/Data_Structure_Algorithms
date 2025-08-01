# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if l1 is None and l2 is None:
            return None
        
        new_node = ListNode(0)
        temp = new_node
        carry = 0
        while l1 or l2:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry
            carry = total // 10
            digit = total % 10

            temp.next = ListNode(digit) 
            temp = temp.next
            
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            
        if carry:
            temp.next = ListNode(carry)
        return new_node.next

