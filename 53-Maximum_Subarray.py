class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSum =  0   
        maxSum = nums[0]
        for n in nums:
            if curSum < 0:  #to remove negative prefix , if we encounter with a negative number then we will make the sum to 0
                curSum = 0
            curSum += n
            if curSum > maxSum:  #updating
                maxSum = curSum
        return maxSum
# Time: O(n)
# Kadane's Algorithm
