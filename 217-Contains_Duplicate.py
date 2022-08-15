# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
# Approach 1: Brute force solution. Time: O(n^2) Space : O(1)
# Approach 2: Sorting the array. Time: O(nlogn) Space: O(1)
# Approach 3: HashSet Time: O(n) Space: O(n)
# Solution using HashSet

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        Set = set()
        
        for n in nums:
            if n in Set:
                return True
            Set.add(n)
        return False
            
