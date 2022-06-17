"""
https://takeuforward.org/data-structure/minimum-number-of-platforms-required-for-a-railway/
https://practice.geeksforgeeks.org/problems/minimum-platforms-1587115620/1#
https://www.codingninjas.com/codestudio/problems/799400?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website
"""
"""
Time Complexity: O(nlogn) Sorting takes O(nlogn) and traversal of arrays takes O(n) so overall time complexity is O(nlogn).

Space complexity: O(1)  (No extra space used).
"""
from sys import stdin, setrecursionlimit
setrecursionlimit(10**7)

def calculateMinPatforms(at, dt, n):
    at.sort()
    dt.sort()
    platformNeeded = 1
    maxi = 1
    i, j = 1, 0
    while i < n and j < n:
        if at[i] <= dt[j]:
            platformNeeded += 1
            i += 1
        elif at[i] > dt[j]:
            platformNeeded -= 1
            j += 1
        if platformNeeded > maxi:
            maxi = platformNeeded
    return maxi

# Taking the input.
def takeInput():
    n = int(stdin.readline().strip())
    at = list(map(int, stdin.readline().strip().split(" ")))
    dt = list(map(int, stdin.readline().strip().split(" ")))

    return at, dt, n

# Main.
T = int(input())
while (T > 0):
    T -= 1
    at, dt, n = takeInput()
    minNumOfPlatforms = calculateMinPatforms(at, dt, n)
    print(minNumOfPlatforms)