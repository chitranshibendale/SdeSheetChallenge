"""
https://takeuforward.org/data-structure/stock-buy-and-sell/
https://www.youtube.com/watch?v=eMSfBgbiEjk&list=PLgUwDviBIf0rPG3Ictpu74YWBQ1CaBkm2&index=12&ab_channel=takeUforward
https://www.codingninjas.com/codestudio/problems/893405?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
"""
import sys


def maximumProfit(prices):
    n = len(prices)
    maximumProfit = 0
    minimumPrice = sys.maxsize
    for i in range(n):
        minimumPrice = min(minimumPrice, prices[i])
        maximumProfit = max(maximumProfit, prices[i] - minimumPrice)
    return maximumProfit


for _ in range(int(input())):
    n = int(input())
    arr = [int(i) for i in input().split()]
    print(maximumProfit(arr))
