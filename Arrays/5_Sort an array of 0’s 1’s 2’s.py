"""
https://takeuforward.org/data-structure/sort-an-array-of-0s-1s-and-2s/
https://www.youtube.com/watch?v=oaVa-9wmpns&list=PLgUwDviBIf0rPG3Ictpu74YWBQ1CaBkm2&index=3
https://www.codingninjas.com/codestudio/problems/631055?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website
https://leetcode.com/problems/sort-colors/
"""
def sort012(arr, n):
    low = 0
    mid = 0
    high = n - 1
    while mid <= high:
        if arr[mid] == 0:
            arr[mid], arr[low] = arr[low], arr[mid]
            mid += 1
            low += 1
        elif arr[mid] == 1:
            mid += 1
        elif arr[mid] == 2:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1




for _ in range(int(input())):
    n = int(input())
    arr = [int(i) for i in input().split()]
    sort012(arr, n)
    print(arr)
"""
Time Complexity: O(N)

Space Complexity: O(1)
"""