"""
Leetcode Problem 121: Best Time to Buy and Sell Stock

Array prices is provided where prices[i] is the price of a given stock on day i. 
This aims to choose a single day to buy a stock and choosing a different day to sell. 

Return the maximum profit that can be achieved from this transaction.

Input: maxProfit(prices) where prices is a list of integers
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        # buy and sell pointers are used to track the days of transaction.
        buy_pointer = 0
        sell_pointer = 1 # sell pointer will always be ahead of buy pointer.

        while sell_pointer < len(prices):
            currProfit = prices[sell_pointer] - prices[buy_pointer]
            if prices[sell_pointer] > prices[buy_pointer]:
                profit = max(profit,currProfit)
            else:
                buy_pointer = sell_pointer
            sell_pointer += 1
        return profit