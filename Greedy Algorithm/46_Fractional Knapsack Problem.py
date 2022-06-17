"""
https://takeuforward.org/data-structure/fractional-knapsack-problem-greedy-approach/
https://practice.geeksforgeeks.org/problems/fractional-knapsack-1587115620/1
https://www.codingninjas.com/codestudio/problems/975286?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website
"""
def maximumValue(items, n, w):
    items.sort(key=lambda x:x[1]/x[0], reverse=True)
    currWeight = 0
    finalValue = 0
    for i in range(n):
        if currWeight + items[i][0] <= w:
            currWeight += items[i][0]
            finalValue += items[i][1]
        else:
            remain = w - currWeight
            finalValue += (items[i][1] / items[i][0]) * remain
            break
    return round(finalValue, 2)
"""
Time Complexity: O(n log n + n). O(n log n) to sort the items and O(n) to iterate through all the items for calculating the answer.

Space Complexity: O(1), no additional data structure has been used.
"""



