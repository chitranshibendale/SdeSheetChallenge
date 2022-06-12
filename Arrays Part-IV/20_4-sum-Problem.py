"""
https://www.youtube.com/watch?v=4ggF3tXIAp0&list=PLgUwDviBIf0p4ozDR_kJJkONnb1wdx2Ma&index=22&ab_channel=takeUforward
https://takeuforward.org/data-structure/4-sum-find-quads-that-add-up-to-a-target-value/
https://leetcode.com/problems/4sum/
https://www.codingninjas.com/codestudio/problems/983605?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website
"""
# leetcode
def fourSum(arr, target):
    arr.sort()
    n = len(arr)
    res = []
    if n == 0:
        return [[]]
    for i in range(n):
        target3 = target - arr[i]
        for j in range(i+1, n):
            target2 = target3 - arr[j]
            front = j + 1
            back = n - 1
            while front < back:
                twoSum = arr[front] + arr[back]
                if twoSum < target2:
                    front += 1
                elif twoSum > target2:
                    back -= 1
                else:
                    temp = [0] * 4
                    temp[0] = arr[i]
                    temp[1] = arr[j]
                    temp[2] = arr[front]
                    temp[3] = arr[back]
                    if temp not in res:
                        res.append(temp)
                    while front < back and arr[front] == temp[2]:
                        front += 1

                    while front < back and arr[back] == temp[3]:
                        back -= 1

            while (j + 1 < n) and arr[j + 1] == arr[j]:
                j += 1
        while (i + 1) < n and arr[i + 1] == arr[i]:
            i += 1
    return res




for _ in range(int(input())):
    n, target = map(int, input().split())
    arr = [int(i) for i in input().split()]
    print(fourSum(arr, target))

"""Time Comlexity : O(n^3), SC : O(1)"""

