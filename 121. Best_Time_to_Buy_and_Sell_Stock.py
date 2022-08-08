class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #Dynamic Sliding Window: Two Pointers Technique 
        l,r = 0,1 #l for buying and r for selling
        MaxProfit = 0 #Initially
        
        while r< len(prices):   #loop to iterate through all the way to the array
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                MaxProfit = max(MaxProfit,profit)  #check if the max profit is greater than the current profit
            else:
                l = r  #l pointer to the end of the array
            r += 1  #if not found, increment r by 1

        return MaxProfit
        
# Memory: O(1)
# Time: O(n)
