"""
https://www.youtube.com/watch?v=S6rsAlj_iB4&list=PLgUwDviBIf0rPG3Ictpu74YWBQ1CaBkm2&index=20&ab_channel=takeUforward
https://www.codingninjas.com/codestudio/problems/1112652?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website
https://leetcode.com/problems/reverse-pairs/
https://takeuforward.org/data-structure/count-reverse-pairs/
"""
def _mergeSort(arr, low, high):
    if low == high:
        return 0
    mid = (low + high) // 2
    inversion = _mergeSort(arr, low, mid)
    inversion += _mergeSort(arr, mid + 1, high)
    inversion += merge(arr, low, mid, high)
    return inversion

def merge(arr, low, mid, high):
    count = 0
    j = mid + 1
    for i in range(low, mid + 1):
        while j <= high and arr[i] > (2 * arr[j]):
            j += 1
        count += (j - (mid + 1))
    temp = []
    left = low
    right = mid + 1
    while left <= mid and right <= high:
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            right += 1
    while left <= mid:
        temp.append(arr[left])
        left += 1
    while right <= high:
        temp.append(arr[right])
        right += 1
    for i in range(low, high + 1):
        arr[i] = temp[i - low]
    return count



def reversePairs(arr, n):
    return _mergeSort(arr, 0, n - 1)

for _ in range(int(input())):
    n = int(input())
    arr = [int(i) for i in input().split()]
    print(reversePairs(arr, n))