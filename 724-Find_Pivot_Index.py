class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        left_sum = 0
        for i in range(len(nums)):
            right_sum = total - left_sum - nums[i]   #for calculating the right side, we are subtracting the total of the array with left side sum and the the slected pivot element
            if left_sum == right_sum:
                return i
            left_sum += nums[i]
        return -1
 # Time : O(n)  Space: O(1)
