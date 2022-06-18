"""
https://takeuforward.org/data-structure/n-queen-problem-return-all-distinct-solutions-to-the-n-queens-puzzle/
https://leetcode.com/problems/n-queens/
https://www.codingninjas.com/codestudio/problems/759332?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website
"""
def isSafe(row, column, chessBoard, n):
    # vertical direction
    i = row - 1
    while i >= 0:
        if chessBoard[i][column] == 1:
            return False
        i -= 1
    # upper left diagonal
    i = row - 1
    j = column - 1
    while i >= 0 and j >= 0:
        if chessBoard[i][j] == 1:
            return False
        i -= 1
        j -= 1
    # upper right diagonal
    i = row - 1
    j = column + 1
    while i >= 0 and j < n:
        if chessBoard[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True

def printPaths(row, n, chessBoard, ans):

    if row == n:
        temp = []
        for i in range(n):
            for j in range(n):
                temp.append(chessBoard[i][j])
        ans.append(temp)
        return

    for column in range(n):
        if isSafe(row, column, chessBoard, n):
            chessBoard[row][column] = 1
            printPaths(row+1, n, chessBoard, ans)
            chessBoard[row][column] = 0

    return

def solveNQueens(n):
    # Implement Your Code Here
    chessBoard = [[0 for j in range(n)] for i in range(n)]
    ans = []
    printPaths(0, n, chessBoard, ans)
    return ans




n = int(input())
print(solveNQueens(n))