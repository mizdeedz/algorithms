# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# Find the maximum profit you can achieve.
# You may complete as many transactions as you like (buy one and sell one share of the stock multiple times).

# Example: prices = [7, 1, 5, 3, 6, 4], Return: 7
# Explanation: Buy on the day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4
# Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
# Last, add them together: Trade 1 profit (4) + Trade 2 profit (3) = 7 (max profit)


# Solution #1
# O(n)

def buy_and_sell_stock_2(prices):
    profit = 0

    for i in range(len(prices) - 1):
        if prices[i + 1] > prices[i]:
            profit = profit + prices[i + 1] - prices[i]

    return profit


test_prices = [7, 1, 5, 3, 6, 4]
print(buy_and_sell_stock_2(test_prices))
