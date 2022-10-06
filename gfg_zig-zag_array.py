class Solution:

	def zigZag(self,arr, n):
	    flag = True
        for i in range(n-1):
        
            if flag is True:
                if arr[i] > arr[i+1]:
                    arr[i], arr[i+1] = arr[i+1], arr[i]
                else:
                    if arr[i] < arr[i+1]:
                        arr[i], arr[i+1] = arr[i+1], arr[i]
                flag = bool(1 - flag)
        print(arr)
# Time: O(n) Space: O(1)
