"""
https://leetcode.com/problems/remove-duplicates-from-sorted-array/
https://www.youtube.com/watch?v=Fm_p9lJ4Z_8&list=PLgUwDviBIf0p4ozDR_kJJkONnb1wdx2Ma&index=44&ab_channel=takeUforward
https://www.codingninjas.com/codestudio/problems/1102307?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website
https://takeuforward.org/data-structure/remove-duplicates-in-place-from-sorted-array/
"""
def removeDuplicates(arr,n):
    if n == 0:
        return 0
    i = 0
    for j in range(n):
        if arr[j] != arr[i]:
            i += 1
            arr[i] = arr[j]
    return i + 1

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    print(removeDuplicates(arr, n))