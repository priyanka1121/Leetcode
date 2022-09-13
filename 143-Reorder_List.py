# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# we are doing like first we divide the linked list in to two parts , the put it in the sort of array 
# make 2 pointer slow and fast two find middle and then reverse the second half becasue we want the last node to be second like the second half will be merged with the first half like we put it in alternative position in first half
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Find middle
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # Reverse the second half 
        second = slow.next
        prev = slow.next = None   # prev initially null
        while second:     #reversing the second list
            temp = second.next
            second.next = prev
            prev = second
            second = temp
            
        # merging the two halfs
        first, second = head, prev
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2
            
   # Time : O(n), Space: O(n)
