from typing import List, Optional


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maximized_profit: int = 0
        current_holding_price: Optional[int] = prices[0]

        for today_price in prices[1:]:
            if current_holding_price < today_price:
                maximized_profit += today_price - current_holding_price
            current_holding_price = today_price

        ## More verbose and suboptimal Solution
        # inclining_days: List[bool] = []
        # for idx, price in enumerate(prices[: len(prices)-1]):
        #     if price < prices[idx+1]:
        #         inclining_days.append(True)
        #     else:
        #         inclining_days.append(False)

        # inclining_days.append(False) # Should sell if holding stock on the last day

        # print(inclining_days)

        # for day, is_inclining in enumerate(inclining_days):
        #     print(f"{day} {is_inclining} {current_holding_price} {maximized_profit}")
        #     if is_inclining:
        #         if current_holding_price is None:
        #             current_holding_price = prices[day]
        #         else:
        #             pass
        #     else:
        #         if current_holding_price is None:
        #             pass
        #         else:
        #             maximized_profit += prices[day] - current_holding_price
        #             current_holding_price = None

        return maximized_profit
