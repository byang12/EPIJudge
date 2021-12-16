class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # no need for DP, simple greedy algorithm
        if len(prices) == 1:
            return 0
        previous_element = prices[0]
        profit_so_far = 0
        for i in range(1,len(prices)):
            price_Change = prices[i] - previous_element
            if price_Change > 0:
                profit_so_far = profit_so_far + price_Change
            previous_element = prices[i]
        return profit_so_far
