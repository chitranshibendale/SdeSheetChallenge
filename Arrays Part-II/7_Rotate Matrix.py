"""
https://takeuforward.org/data-structure/rotate-image-by-90-degree/
https://www.youtube.com/watch?v=Y72QeX0Efxw&list=PLgUwDviBIf0rPG3Ictpu74YWBQ1CaBkm2&index=13&ab_channel=takeUforward
https://www.codingninjas.com/codestudio/problems/981260?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website
https://leetcode.com/problems/rotate-image/
"""
def rotateMatrix(mat, n, m):           #Codestudio

    top = 0
    bottom = n - 1
    left = 0
    right = m - 1
    while left < right and top < bottom:
        prev = mat[top+1][left]
        for i in range(left, right + 1):
            curr = mat[top][i]
            mat[top][i] = prev
            prev = curr
        top += 1
        for i in range(top, bottom + 1):
            curr = mat[i][right]
            mat[i][right] = prev
            prev = curr
        right -= 1
        for i in range(right, left - 1, -1):
            curr = mat[bottom][i]
            mat[bottom][i] = prev
            prev = curr
        bottom -= 1
        for i in range(bottom, top - 1, -1):
            curr = mat[i][left]
            mat[i][left] = prev
            prev = curr
        left += 1


def rotateMatrix1(mat, n, m):           #Leetcode

    for i in range(n):
        for j in range(i):
            mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
    for i in range(n):
        mat[i].reverse()


    # Write your code here


for _ in range(int(input())):
    row, col = map(int, input().split())
    matrix = []
    for i in range(row):
        arr = [int(i) for i in input().split()]
        matrix.append(arr)
    rotateMatrix(matrix, row, col)
    print(matrix)