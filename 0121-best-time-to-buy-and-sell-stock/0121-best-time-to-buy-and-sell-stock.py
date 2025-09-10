class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result=0
        j=0
        for i in range(len(prices)):
            if prices[i]>prices[j]:
                result=max(result,prices[i]-prices[j]) 
            elif prices[i]<prices[j]:
                j=i
        #     for j in range(i,len(prices)):
        #         if prices[j]>prices[i]:
        #             result=max(result,prices[j]-prices[i])
        return result
        