"""https://takeuforward.org/data-structure/set-matrix-zero/
Codestudio : https://www.codingninjas.com/codestudio/problems/set-matrix-zeros_3846774?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website&leftPanelTab=0
Leetcode: https://leetcode.com/problems/set-matrix-zeroes/
"""

"""OPTIMAL SOLUTION """

def setZeros(matrix):
    zerothColumn = True
    row = len(matrix)
    col = len(matrix[0])
    for i in range(row):
        if matrix[i][0] == 0:
            zerothColumn = False
        for j in range(1, col):
            if matrix[i][j] == 0:
                matrix[i][0] = matrix[0][j] = 0
    for i in range(row - 1, -1, -1):
        for j in range(col - 1, 0, -1):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0
        if zerothColumn == False:
            matrix[i][0] = 0

for _ in range(int(input())):
    n, m = map(int, input().split())
    matrix = []
    for i in range(n):
        arr = [int(i) for i in input().split()]
        matrix.append(arr)
    setZeros(matrix)
    print(matrix)

"""
TC : 2 * O(n * m)
SC : O(1)
"""


