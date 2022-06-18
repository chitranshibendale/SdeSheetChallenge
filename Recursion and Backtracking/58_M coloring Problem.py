"""
https://www.codingninjas.com/codestudio/problems/981273?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website
https://takeuforward.org/data-structure/m-coloring-problem/
https://practice.geeksforgeeks.org/problems/m-coloring-problem-1587115620/1#
"""


def isSafe(node, color, n, mat, col):
    for k in range(n):
        if k != node and mat[node][k] == 1 and color[k] == col:
            return False
    return True


def solve(node, color, mat, n, m):
    if node == n:
        return True
    for i in range(1, m + 1):
        if isSafe(node, color, n, mat, i):
            color[node] = i
            if solve(node + 1, color, mat, n, m):
                return True
            color[node] = 0

    return False


def graphColoring(mat, m):
    n = len(mat)
    color = [0 for i in range(n)]
    if solve(0, color, mat, n, m):
        return "YES"
    return "NO"

    # Your code goes here

# Your code goes here



