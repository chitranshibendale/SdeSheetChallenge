"""
https://www.geeksforgeeks.org/find-minimum-number-of-coins-that-make-a-change/
https://www.codingninjas.com/codestudio/problems/975277?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website
https://takeuforward.org/data-structure/find-minimum-number-of-coins/
"""
"""
Time Complexity:O(V)

Space Complexity:O(1)
"""
denominations = [1, 2, 5, 10, 20, 50, 100, 500, 1000]


def findMinimumCoins(amount):
    mini = 0
    n = len(denominations)
    j = n - 1
    while amount > 0:
        if denominations[j] > amount:
            j -= 1
        else:
            mini += 1
            amount = amount - denominations[j]
    return mini


for _ in range(int(input())):
    amount = int(input())
    print(findMinimumCoins(amount))