"""
https://takeuforward.org/data-structure/program-to-generate-pascals-triangle/
https://www.codingninjas.com/codestudio/problems/1089580?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website
https://leetcode.com/problems/pascals-triangle/
https://www.youtube.com/watch?v=6FLvhQjZqvM&list=PLgUwDviBIf0rPG3Ictpu74YWBQ1CaBkm2&index=9&ab_channel=takeUforward
"""
def printPascal(n):
    res = [[1]]
    for i in range(n-1):
        temp = [0] + res[-1] + [0]
        row = []
        for j in range(len(res[-1]) + 1):
            row.append(temp[j] + temp[j+1])
        res.append(row)
    return res

    # Write your code here.
    # Return a list of lists.
for _ in range(int(input())):
    n = int(input())
    print(printPascal(n))
"""
Given row (r) number and column(c) no. Tell the value at that number
Formula =>
r-1
    C
      c-1

TC: O(n)
SC : O(1)  
----
"""