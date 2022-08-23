#Approach 1: Sorting but time: O(n log n)
#Approach 2: Iterate through the array -> Use a set  -> check whether the value have left neighbours and if they have start the sequence.
#Time: O(n) Space: O(n)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for n in nums:
            # check if its the start of a sequence
            if (n - 1) not in numSet:
                length = 1
                while (n + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest
