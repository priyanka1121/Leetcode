#Solution using HashMap

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Map = {} #mapping the value to the index of that value. Previous value is going to be mapped
        for i, n in enumerate(nums):   
            dif = target - n 
            if dif in Map:  #if the difference is already in the map return the solution 
                return [Map[dif],i]
            Map[n] = i #if dont continue it
        return
        
#complexity of O(n)
