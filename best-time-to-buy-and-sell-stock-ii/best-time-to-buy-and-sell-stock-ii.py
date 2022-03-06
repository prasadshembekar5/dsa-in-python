class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #Initialize Profit to zero 
        profit = 0 
        #We will compare value with previousw one 
        #so range it from 1 to length of prices array  
        for i in range(1,len(prices)): 
            if prices[i] > prices[i-1]: #current val is more than prev one its profit 
                profit += (prices[i] - prices[i-1]) #Calculate profit 
                #by substracting cur price and prev price
        return profit 