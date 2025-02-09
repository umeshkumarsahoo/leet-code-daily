class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price=prices[0]
        maxim_profit=0
        for price in prices[1:]:
            min_price=min(min_price,price)
            maxim_profit=max(maxim_profit,price-min_price)
        return maxim_profit
       

            
            
