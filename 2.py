"""This problem was asked by Facebook.
Given an array of numbers representing the stock prices of a company in chronological order,
 write a function that calculates the maximum profit you could have made from buying and selling that stock once.
  You must buy before you can sell it.
For example, given [9, 11, 8, 5, 7, 10], you should return 5,
since you could buy the stock at 5 dollars and sell it at 10 dollars."""


# [9,11,6,8,7,10]

def stock_prices(stocks):
    min_price = min(stocks)
    arr = stocks[min_price-1::]
    sell_price = max(arr)
    print(sell_price - min_price)


stock_prices([9, 11, 6, 5, 7, 10])
