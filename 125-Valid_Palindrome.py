#Solution 1: Remving all the space and special characters and converting into lower case and then check if its palindrome
class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = "" #removing all the special character
        
        for c in s:
            if c.isalnum():
                new += c.lower()
        return new == new[::-1]
        

#problem: We use extra memory by building a new strings and a predefined function to check alphanymeric character


class Solution:
    def isPalindrome(self, s: str) -> bool:
        #taking two pointers left and right and len-1 
        l,r = 0 , len(s)-1
        
        while l<r:
            #condition to check if the character is alphaumeric or not and l<r and r>l to make sure everything is balanced on both side
            while l<r and not self.AlphaNum(s[l]):
                l += 1
                #if it does it will increment and go to next character
            while r>l and not self.AlphaNum(s[r]):
                r -= 1
            #from the right side, it will decrement 
            
            if s[l].lower() != s[r].lower():
                return False
             #if condition to check the left and right are not equal and character have to be in lowerCase
                
            #after check increment and decrement the pointers
            l,r = l+1, r-1
        return True
        
    def AlphaNum(self,c):
        return (ord('A')<= ord(c) <= ord('Z')or
               ord('a')<= ord(c) <= ord('z')or
               ord('0')<= ord(c) <= ord('9'))
# Time: O(n), space: O(1)
