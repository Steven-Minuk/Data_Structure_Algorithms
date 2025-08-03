# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Otional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if list1 == None and list2 == None:
            return None
        
        if list1 == None:
            return list2
        
        if list2 == None:
            return list1

        #initialize
        if list1.val <= list2.val:
            head = list1
            list1 = list1.next
        else:
            head = list2
            list2 = list2.next
        tail = head
        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            elif list1.val > list2.val:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
        
        return head

alist = ListNode(1)
alist.next = ListNode(2)
alist.next.next = ListNode(4)

blist = ListNode(1)
blist.next = ListNode(3)
blist.next.next = ListNode(4)

solution = Solution()
solution.mergeTwoLists(alist, blist)
