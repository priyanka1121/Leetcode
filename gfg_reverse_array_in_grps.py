class Solution:	
    #Function to reverse every sub-array group of size k.
	def reverseInGroups(self, arr, n, k):
	    i = 0
	    while(i<n):  #base case: If k = 1, the array should remain unchanged. If k >= n, we reverse all elements present in the array.
	        left = i
	        right = min(i+k-1,n-1)  #base case
	        
	        while(left < right):
	            arr[left],arr[right]=arr[right],arr[left] #reversing 
	            left +=1
	            right -=1
	        i+=k
		
 # Time: O(n) Space:O(1) Approach: Two Pointers
