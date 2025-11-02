class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = float('inf')
        sell = 0

        for price in prices:
            if price < buy:
                buy = price
            elif price - buy > sell:
                sell = price - buy
            
        return sell