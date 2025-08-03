# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        if head is None:
            return None
        
        if n == 0:
            return head

        count = 0
        temp = head
        while temp is not None:
            count += 1
            temp = temp.next
        
        if count == n:
            return head.next

        count -= n
        count -= 1
        temp2 = head
        for i in range(count):
            temp2 = temp2.next
        
        if temp2.next:
            temp2.next = temp2.next.next

        return head