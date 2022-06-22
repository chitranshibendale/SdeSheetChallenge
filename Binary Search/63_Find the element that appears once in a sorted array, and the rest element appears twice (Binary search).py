"""
https://leetcode.com/problems/single-element-in-a-sorted-array/
https://www.codingninjas.com/codestudio/problems/1112654?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website
https://takeuforward.org/data-structure/search-single-element-in-a-sorted-array/
"""


def uniqueElement(arr, n):
    if n == 1:
        return arr[0]
    if arr[0] != arr[1]:
        return arr[0]
    if arr[-1] != arr[-2]:
        return arr[-1]
    l = 0
    h = n - 1
    while l <= h:
        mid = (l + h) // 2
        if arr[mid] != arr[mid - 1] and arr[mid] != arr[mid + 1]:
            return arr[mid]
        elif arr[mid] == arr[mid - 1]:
            leftCount = mid - l + 1
            if leftCount % 2 == 0:
                l = mid + 1
            else:
                h = mid - 2
        elif arr[mid] == arr[mid + 1]:
            rightCount = h - mid + 1
            if rightCount % 2 == 0:
                h = mid - 1
            else:
                l = mid + 2

