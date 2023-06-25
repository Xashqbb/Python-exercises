class Solution(object):
    def maxProfit(self, prices):
        if not prices:
            return 0
        minprice=prices[0]
        max_profit=0
        for price in prices:
            if price < minprice:
                minprice = price
            elif price - minprice > max_profit:
                max_profit = price - minprice

        return max_profit