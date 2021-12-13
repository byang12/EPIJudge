from typing import List

from test_framework import generic_test


def buy_and_sell_stock_once(prices: List[float]) -> float:
    # TODO - you fill in here.
    max_profit = 0.0
    lowest_price_so_far = prices[0]
    for i in range(1,len(prices)):
        today_profit = prices[i] - lowest_price_so_far
        max_profit = max(max_profit,today_profit)
        lowest_price_so_far = min(lowest_price_so_far,prices[i])
    return max_profit


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock.py',
                                       'buy_and_sell_stock.tsv',
                                       buy_and_sell_stock_once))
