""""
https://www.youtube.com/watch?v=hVl2b3bLzBw&list=PLgUwDviBIf0rPG3Ictpu74YWBQ1CaBkm2&index=5&ab_channel=takeUforward
https://www.codingninjas.com/codestudio/problems/1214628?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website
https://leetcode.com/problems/merge-sorted-array/
"""

import math

def ninjaAndSortedArrays(arr1,arr2,n, m):
    n = len(arr1)
    m = len(arr2)
    gap = math.ceil((n+m)/2)
    while gap > 0:
        i = 0
        j = gap
        while j < (n + m):
            if j < n and arr1[i] > arr1[j]:
                arr1[i], arr1[j] = arr1[j], arr1[i]
            elif j >= n and i < n and arr1[i] > arr2[j - n]:
                arr1[i], arr2[j-n] = arr2[j-n], arr1[i]
            elif j >= n and i >= n and arr2[i - n] > arr2[j - n]:
                arr2[i - n], arr2[j - n] = arr2[j - n], arr2[i - n]
            j += 1
            i += 1
        if gap == 1:
            gap = 0
        else:
            gap = math.ceil(gap/2)


for _ in range(int(input())):
    m, n = map(int, input().split())
    arr1 = [int(i) for i in input().split()]
    arr2 = [int(i) for i in input().split()]
    ninjaAndSortedArrays(arr1, arr2, m, n)
    print(arr1)
    print(arr2)
