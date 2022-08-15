 # Approach 1: Use Hashmap 
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #return Counter(s) == Counter(t)
       
        
        #if length of strings are not equal
        
        if len(s) != len(t):
            return False
        
        #Define Hash maps for both of strings
        countS, countT = {}, {}
        
        #creating the hash maps
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i],0)
            countT[t[i]] = 1 + countT.get(t[i],0)
        #if count is not equal
        for c in countS:
            if countS[c] != countT.get(c,0):
                return False
        return True
# Time: O(n) or O(s+t)
# Space: O(s+t)

#Approach 2: Sorting both string and then comparing it

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        return sorted(s) == sorted(t)
        
