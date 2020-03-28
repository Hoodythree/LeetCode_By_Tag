# Input: [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
#              Not 7-1 = 6, as selling price needs to be larger than buying price.

# brute force
# def maxProfit(prices):
#     maxprofit = 0
#     for i in range(len(prices)):
#         for j in range(i+1, len(prices)):
#             if prices[j] - prices[i] > maxprofit:
#                 maxprofit = prices[j] - prices[i]
#     return maxprofit
def maxProfit(prices):
    maxprofit = 0
    minimal = float('inf')
    for i in range(len(prices)):
        if prices[i] < minimal:
            minimal = prices[i]
        elif prices[i] - minimal > maxprofit:
            maxprofit = prices[i] - minimal
    return maxprofit

prices = [7,1,5,3,6,4]
print(maxProfit(prices))
