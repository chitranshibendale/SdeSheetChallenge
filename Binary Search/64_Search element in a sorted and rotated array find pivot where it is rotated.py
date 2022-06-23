"""
https://www.codingninjas.com/codestudio/problems/630450?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website&leftPanelTab=1
https://leetcode.com/problems/search-in-rotated-sorted-array/
https://takeuforward.org/data-structure/search-element-in-a-rotated-sorted-array/
"""
def search(arr, target):
    n = len(arr)
    i = 0
    j = n - 1
    while i <= j:
        mid = (i + j) // 2
        if arr[mid] == target:
            return mid
        if arr[0] <= arr[mid]:
            if target >= arr[i] and target <= arr[mid]:
                j = mid - 1
            else:
                i = mid + 1
        else:
            if target >= arr[mid] and target <= arr[j]:
                i = mid + 1
            else:
                j = mid - 1

    return -1

for _ in range(int(input())):
    arr = [int(i) for i in input().split()]
    q = int(input())
    for i in range(q):
        print(search(arr, i))