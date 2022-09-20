class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        c = [A[len(A)-1]]   #creating a variable to store rightmost leader
        m = A[len(A)-1]      #creating max for storing max number while traversing (initial max: A-1)
        for i in range(len(A)-2,-1,-1):  #travesing from the right
            if m<A[i]:   #if current element greater than max 
                c.append(A[i]) #add in c
                m=A[i]    #update m with greater value
        return c
      
      
      # Time: O(n) Space:O(1)
