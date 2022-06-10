"""
https://takeuforward.org/interviews/strivers-sde-sheet-top-coding-interview-problems/
https://www.codingninjas.com/codestudio/problems/893027?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website
https://www.youtube.com/watch?v=1QybAZMCYhA&ab_channel=Pepcoding
https://leetcode.com/problems/majority-element-ii/
https://takeuforward.org/data-structure/majority-elementsn-3-times-find-the-elements-that-appears-more-than-n-3-times-in-the-array/
"""
def majorityElementII(arr):
    value1 = -1
    count1 = 0
    value2 = -1
    count2 = 0
    n = len(arr)
    for i in range(n):
        if arr[i] == value1:
            count1 += 1
        elif arr[i] == value2:
            count2 += 1
        elif count1 == 0:
            value1 = arr[i]
            count1 = 1
        elif count2 == 0:
            value2 = arr[i]
            count2 = 1
        else:
            count1 -= 1
            count2 -= 1
    count1, count2 = 0, 0
    ans = []
    for i in range(n):
        if arr[i] == value1:
            count1 += 1
        elif arr[i] == value2:
            count2 += 1
    if count1 > n // 3:
        ans.append(value1)
    if count2 > n // 3:
        ans.append(value2)
    return ans



for _ in range(int(input())):
    n = int(input())
    arr = [int(i) for i in input().split()]
    print(majorityElementII(arr))

    """
Time Complexity: O(n)

Space Complexity: O(1)
    """