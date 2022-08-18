# Technique: Bit manipulation using XOR operator
# use exclusive or operation to filter out all the values that appear twice, 
# since every number does exclusive or with itself will always result in zero, the single number that appears only once will be the one that's left out.
# which result in linear runtime without any extra memory

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        out =  0 # n ^ 0 = n (XOR)
        for n in nums:
            out = n^out
        return out
      
#Time: O(n), Memory: O(1)
