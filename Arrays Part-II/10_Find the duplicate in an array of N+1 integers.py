"""
https://takeuforward.org/data-structure/find-the-duplicate-in-an-array-of-n1-integers/
https://www.youtube.com/watch?v=32Ll35mhWg0&list=PLgUwDviBIf0rPG3Ictpu74YWBQ1CaBkm2&index=2&ab_channel=takeUforward
https://www.codingninjas.com/codestudio/problems/1112602?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website
https://leetcode.com/problems/find-the-duplicate-number/
https://www.youtube.com/watch?v=wjYnzkAhcNk&ab_channel=NeetCode
"""
# floyd's algo
def findDuplicate(arr:list, n:int):
    slow, fast = 0, 0
    while True:
        slow = arr[slow]
        fast = arr[arr[fast]]

        if slow == fast:
            break
    slow2 = 0
    while True:
        slow = arr[slow]
        slow2 = arr[slow2]
        if slow == slow2:
            break
    return slow

    # Write your code here.
    # Returns an integer.

for _ in range(int(input())):
    n = int(input())
    arr1 = [int(i) for i in input().split()]
    print(findDuplicate(arr1, n))

# Solution : Linked List using Floyd Cycle Detection Algorithm
# Time Complexity : O(n)
# Space Complexity : O(1)