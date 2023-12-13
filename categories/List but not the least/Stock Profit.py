"""
Your function needs to analyze the price fluctuations of the stock over time.
It should identify the most profitable opportunity by calculating the maximum potential profit achievable within these
fluctuations. This means finding the highest price to sell the stock after buying it at the lowest possible price.

However, if there's no possibility to make a profit—such as when the stock price consistently decreases or
remains the same—the function should return zero,
indicating that there's no viable opportunity for a profitable transaction.

assert stock_profit([2, 3, 4, 5]) == 3
assert stock_profit([3, 1, 3, 4, 5, 1]) == 4
assert stock_profit([4, 3, 2, 1]) == 0
assert stock_profit([6, 2, 1, 2, 3, 2, 3, 4, 5, 4]) == 4
https://py.checkio.org/en/mission/stock-profit/
"""


def stock_profit(stock: list[int]) -> int:
    min_value = min(stock[:-1])
    index_min = stock.index(min_value)
    max_value = max(stock[index_min:])
    return max_value - min_value


print("Example:")
print(stock_profit([3, 1, 3, 4, 5, 1]))

# These "asserts" are used for self-checking
assert stock_profit([2, 3, 4, 5]) == 3
assert stock_profit([3, 1, 3, 4, 5, 1]) == 4
assert stock_profit([4, 3, 2, 1]) == 0
assert stock_profit([6, 2, 1, 2, 3, 2, 3, 4, 5, 4]) == 4
assert stock_profit([1, 1, 1, 2, 1, 1, 1]) == 1
assert stock_profit([4, 3, 2, 1, 2, 1, 2, 1]) == 1
assert stock_profit([1, 1, 1, 1]) == 0

print("You are the best broker here! Click 'Check' to earn cool rewards!")
