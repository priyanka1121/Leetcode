# Time: O(n) Space: O(1)
# Going to use postfix and prefix method to get the result
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        #prefix and postfix as pre and post 
        out = [1] * (len(nums))  # result array
        
        pre = 1    #default value for prefix
        for i in range(len(nums)):  #going through input array (->)
            out[i] = pre
            pre *= nums[i]
            
        post = 1  #default value for postfix
        for i in range(len(nums) -1,-1,-1):  #going thorugh input array (<-)
            out[i] *= post
            post *= nums[i]
        return out
