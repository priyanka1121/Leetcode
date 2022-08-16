# Soving th problem in linear time o(n) through dictinary
# Making an array which store the counts of eacg elements
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = {}  #Hashamp
        f = [[] for i in range(len(nums) + 1)]  #Empty array and this is goung to be the size of the input + 1
        
        for n in nums:  #going through every value and count its occurence
            count[n] = 1 + count.get(n,0) # 0 for default value if doesn't exist
        for n,c in count.items():  #going through each value we counted
            f[c].append(n)   #this value of n occurs exactly c no. of times
            
        out = []   #result array
        for i in range(len(f) -1,0,-1):  #iterating through in descending order in array
            for n in f[i]:
                out.append(n)
                if len(out) == k:
                    return outa
                
#Time: O(n) Space: O(n)
