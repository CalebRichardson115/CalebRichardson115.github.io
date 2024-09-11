#Leetcode 122. Simpler version of 121 as this allows for buying/selling on multiple days.
class Solution(object):
    def maxProfit(self, prices):
        max = 0
        for i in range(len(prices)):
            if i != 0 and prices[i] > prices[i-1]:
                max += prices[i]-prices[i-1]
        return max