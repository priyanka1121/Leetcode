#Using hashap, First going to make an array to count the charcters and store their combinations in a hashmap and show it as the output
# Time: O(m.n) where m is given input strings and n is average length of the string

class Solution(object):
    def groupAnagrams(self, strs):
        out = defaultdict(list) # mapping the character count to list of anagrams and defaultdict for edge case 
        
        for s in strs:
            count = [0] * 26 # a - z 
            for c in s:     #go through every single character and count how many of each character
                count[ord(c)-ord("a")] += 1
                
            out[tuple(count)].append(s)  #group strings for the particular count together
                
        return out.values()
