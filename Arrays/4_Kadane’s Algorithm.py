"""
https://takeuforward.org/data-structure/kadanes-algorithm-maximum-subarray-sum-in-an-array/
https://www.youtube.com/watch?v=w_KEocd__20&list=PLgUwDviBIf0rPG3Ictpu74YWBQ1CaBkm2&index=6&ab_channel=takeUforward
https://www.codingninjas.com/codestudio/problems/630526?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website
https://leetcode.com/problems/maximum-subarray/
"""

def maxSubarraySum(arr, n) :
    sum = 0
    maxi = arr[0]
    for i in range(n):
        sum = sum + arr[i]
        if sum > maxi:
            maxi = sum
        if sum < 0:
            sum = 0
    if sum == 0:
        return sum
    return maxi



n = int(input())
arr = [int(i) for i in input().split()]
print(maxSubarraySum(arr, n))

"""
TC : O(n)
Sc : O(1)
"""