# Approach 1: Use Hashmap + Linear Traversal // Time: O(N log N), Space: O(n)
# Approach 2: User sorting + Linear Traversal // Time: O(N log N +N) (log N<=32)
# Approach 3: Counting set Bits becaause every numer will appear three times except only one
# we need 2 bits to save the 3 states of all elements.
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # approach: by drawing truth table for 00 -> 01 -> 10 -> 00
        #           l' = ~h & (l ^ i)
        #           h' = ~l' & (h ^ i)
        
        low= high = 0   #Initialized
        for num in nums:
            low = ~high & (low ^ num)
            high = ~low & (high ^ num)
        return low
    
    
    #Time: O(n), Space: O(1)
