'''
Leetcode 121
Program that returns the best profit given an array of prices on different days.
Evaluates the best price and best time to sell and returns the maximum profit, assuming that
stock can only be bough on one day and sold on another.
'''
class Solution(object):
    def maxProfit(self, prices):
        profit = 0
        bestPrice = prices[0]
        for i in range(len(prices)):
            if prices[i] < bestPrice:
                bestPrice = prices[i]
            elif prices[i] - bestPrice > profit:
                profit = prices[i]-bestPrice
        return profit