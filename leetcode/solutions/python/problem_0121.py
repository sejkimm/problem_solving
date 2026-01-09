from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maximized_profit: int = 0
        min_price: int = prices[0]

        for price in prices[1:]:
            if price < min_price:
                min_price = price
            else:
                maximized_profit = max(maximized_profit, price - min_price)

        return maximized_profit
