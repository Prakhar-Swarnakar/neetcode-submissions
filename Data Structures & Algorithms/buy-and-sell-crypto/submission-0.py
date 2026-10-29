class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minBuy = prices[0]
        maxprofit = 0
        for currPrice in prices:
            profit = currPrice-minBuy
            maxprofit = max(maxprofit, profit)
            minBuy = min(minBuy, currPrice)
        return maxprofit