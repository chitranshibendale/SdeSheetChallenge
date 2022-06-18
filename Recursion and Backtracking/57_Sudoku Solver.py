"""
https://leetcode.com/problems/sudoku-solver/
https://www.codingninjas.com/codestudio/problems/758961?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website
https://takeuforward.org/data-structure/sudoku-solver/
"""
#codestudio
def find_empty_location(board, arr):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                arr[0] = i
                arr[1] = j
                return True
    return False

def usedInRow(board, row, num):
    for i in range(9):
        if board[row][i] == num:
            return True
    return False

def usedInCol(board, col, num):
    for i in range(9):
        if board[i][col] == num:
            return True
    return False

def usedInBox(board, row, col, num):
    for i in range(3):
        for j in range(3):
            if board[i + row][j + col] == num:
                return True
    return False


def checkLocationIsSafe(board, row, col, num):
    ans1 = usedInRow(board, row, num)
    if ans1==True:
        return False
    ans2 = usedInCol(board, col, num)
    if ans2==True:
        return False
    ans3 = usedInBox(board, row - row % 3, col - col % 3, num)
    if ans3==True:
        return False
    return True

def isItSudoku(board):
    arr = [0, 0]
    if find_empty_location(board, arr) is False:
        return True

    row = arr[0]
    col = arr[1]

    for num in range(1, 10):
        if checkLocationIsSafe(board, row, col, num):
            board[row][col] = num
            if isItSudoku(board):
                return True
            board[row][col] = 0
    return False

for _ in range(int(input())):
    board = [[int(ele) for ele in input().split()] for i in range(9)]
    print(isItSudoku(board))