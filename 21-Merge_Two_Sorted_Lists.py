# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        dummy = ListNode()  #To tackle the edge cases
        tail = dummy  

        while list1 and list2:    #While both are non-empty
            if list1.val < list2.val:  #if l1 value are smaller than l2, print l1 value -> we have to print the mergerd list in sorted order 
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        if list1:         #if l2 is empty and only l1 have nodes then this condition print all the nodes of l1
            tail.next = list1
        elif list2:
            tail.next = list2

        return dummy.next


