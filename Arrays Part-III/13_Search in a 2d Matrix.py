"""
https://takeuforward.org/data-structure/search-in-a-sorted-2d-matrix/
https://www.youtube.com/watch?v=ZYpYur0znng&list=PLgUwDviBIf0rPG3Ictpu74YWBQ1CaBkm2&index=15&ab_channel=takeUforward
https://www.codingninjas.com/codestudio/problems/980531?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website
https://leetcode.com/problems/search-a-2d-matrix/
"""
def findTargetInMatrix(mat, m, n, target):
    low = 0
    if m == 0:
        return False
    high = (m * n) - 1
    while low <= high:
        mid = (low + high) // 2
        rowIndex = mid // n
        columnIndex = mid % n
        if mat[rowIndex][columnIndex] == target:
            return True
        if mat[rowIndex][columnIndex] < target:
            low = mid + 1
        else:
            high = mid - 1
    return False

for _ in range(int(input())):
    m, n, target = map(int, input().split())
    mat = []
    for i in range(m):
        row = [int(i) for i in input().split()]
        mat.append(row)
    print(findTargetInMatrix(mat, m, n, target))

"""
Time complexity: O(log(m*n))

Space complexity: O(1)
"""