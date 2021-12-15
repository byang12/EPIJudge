from typing import List

from test_framework import generic_test


def buy_and_sell_stock_twice(prices: List[float]) -> float:
    # TODO - you fill in here.
    max_profit_one_sale = 0.0
    min_price_so_far = prices[0]
    one_sale_profit_list = [0.0]*len(prices)
    for i in range(1,len(prices)):
        max_profit_one_sale = max(max_profit_one_sale,prices[i]-min_price_so_far)
        one_sale_profit_list[i] = max_profit_one_sale
        min_price_so_far = min(prices[i],min_price_so_far)
    
    max_price_so_far = prices[-1]
    max_profit = max_profit_one_sale
    for i in reversed(range(1,len(prices)-1)):
        max_profit = max(max_profit,one_sale_profit_list[i-1]+max_price_so_far-prices[i])
        max_price_so_far = max(prices[i],max_price_so_far)        
    return max_profit


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock_twice.py',
                                       'buy_and_sell_stock_twice.tsv',
                                       buy_and_sell_stock_twice))
