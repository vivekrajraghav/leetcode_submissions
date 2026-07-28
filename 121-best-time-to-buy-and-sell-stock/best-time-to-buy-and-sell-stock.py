class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        min_prices=float("inf")
        max_profit=0
        for i in range(0,n):
            if min_prices>prices[i]:
                min_prices=prices[i]
            if min_prices<prices[i]:
                profit=prices[i]-min_prices
                if profit>max_profit:
                    max_profit=profit
        return max_profit

