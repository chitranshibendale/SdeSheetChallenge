"""
https://www.youtube.com/watch?v=xmguZ6GbatA&list=PLgUwDviBIf0p4ozDR_kJJkONnb1wdx2Ma&index=24&ab_channel=takeUforward
https://practice.geeksforgeeks.org/problems/largest-subarray-with-0-sum/1
https://takeuforward.org/data-structure/length-of-the-longest-subarray-with-zero-sum/
https://www.codingninjas.com/codestudio/problems/920321?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website
"""
def LongestSubsetWithZeroSum(arr):
    n = len(arr)
    d = {}
    sum = 0
    maxi = 0
    for i in range(n):
        sum += arr[i]
        if sum == 0:
            maxi = i + 1
        else:
            if sum not in d:
                d[sum] = i
            else:
                tempMaxi = i - d[sum]
                maxi = max(maxi, tempMaxi)
    return maxi

for _ in range(int(input())):
    n = int(input())
    arr = [int(i) for i in input().split()]
    print(LongestSubsetWithZeroSum(arr))
"""
TC : O(n log n)
SC :O(n)
"""