#iterative approach
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head;
        while curr:
            temp =  curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
        
#Time : O(n) Space: O(1)

# Recursive approach
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        newHead =  head
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head
        head.next = None

        #time: O(n) and Space: O(n)
        
        return newHead
