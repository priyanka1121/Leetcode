# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Slow and fast technique : Floys's tortoise and hare
# Time : O(n)   Space : O(1)

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head    
        
        while fast and fast.next:    #Slow pointer will increased by 1 and fast one increased by 2 and if there is a loop exist the slow and fast will be equal at some point
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
            
            
            
            

        
