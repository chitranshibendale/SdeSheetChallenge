"""
https://leetcode.com/problems/trapping-rain-water/
https://www.codingninjas.com/codestudio/problems/630519?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website
https://takeuforward.org/data-structure/trapping-rainwater/
https://www.youtube.com/watch?v=m18Hntz4go8&list=PLgUwDviBIf0p4ozDR_kJJkONnb1wdx2Ma&index=43&ab_channel=takeUforward
"""
#TC : O(n)
#SC : O(1)
def getTrappedWater(arr, n) :
    left = 0
    right = n - 1
    result = 0
    maxLeft = 0
    maxRight = 0
    while left <= right:
        if arr[left] <= arr[right]:
            if arr[left] >= maxLeft:
                maxLeft = arr[left]
            else:
                result += maxLeft - arr[left]
            left += 1
        else:
            if arr[right] >= maxRight:
                maxRight = arr[right]
            else:
                result += maxRight - arr[right]
            right -= 1
    return result
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    print(getTrappedWater(arr, n))