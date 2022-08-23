#Design an algorithm to encode a list of strings to a strings. The encoded string is then 
# sent over the network and is decoded back to the original list of strings.
# Time: O(n) where n is total number of characters
class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s  #first the length of the string then the delimeter and then the actual string
        return res

    """
    @param: str: A string
    @return: dcodes a single string to a list of strings
    """
    def decode(self, str):
        res, i = [], 0     #Result is a list and a pointer i which tells the position in the list
        
        while i <len(str):
            j = i
            while str[j] != "#":
                j += 1
            length = int(str[i:j]) 
            res.append(str[j+1 : j+1+length]) #read single word
            i = j + 1 + length #beginning of the next string by changin i pointer
        return res
