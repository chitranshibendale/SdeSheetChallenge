"""
https://www.interviewbit.com/problems/matrix-median/
https://www.codingninjas.com/codestudio/problems/873378?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website
"""
def countSmallerThanMid(row, mid):
    l = 0
    h = len(row) - 1
    while l <= h:
        m = (l + h) // 2
        if row[m] <= mid:
            l = m + 1
        else:
            h = m - 1
    return l

def getMedian(matrix):
    low = 1
    high = 1e9
    n = len(matrix)
    m = len(matrix[0])
    while low <= high:
        mid = (low + high) // 2
        count = 0
        for i in range(n):
            count += countSmallerThanMid(matrix[i], mid)
        if count <= (n*m) // 2:
            low = mid + 1
        else:
            high = mid - 1
    return int(low)

for _ in range(int(input())):
    n, m = map(int, input().split())
    matrix = []
    for i in range(n):
        arr = [int(i) for i in input().split()]
        matrix.append(arr)
    print(getMedian(matrix))