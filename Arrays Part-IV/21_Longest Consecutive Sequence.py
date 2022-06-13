""""
https://www.youtube.com/watch?v=qgizvmgeyUM&list=PLgUwDviBIf0p4ozDR_kJJkONnb1wdx2Ma&index=23&ab_channel=takeUforward
https://takeuforward.org/data-structure/longest-consecutive-sequence-in-an-array/
https://www.codingninjas.com/codestudio/problems/759408?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website
https://leetcode.com/problems/longest-consecutive-sequence/
"""
def lengthOfLongestConsecutiveSequence(arr, n):
    maxLength = 0
    d = {}
    for i in arr:
        d[i] = True
    for i in range(n):
        if arr[i] - 1 in d:
            continue
        else:
            tempLength = 0
            ele = arr[i]
            while ele in d:
                tempLength += 1
                ele += 1
            maxLength = max(maxLength, tempLength)
    return maxLength

for _ in range(int(input())):
    n = int(input())
    arr = [int(i) for i in input().split()]
    print(lengthOfLongestConsecutiveSequence(arr, n))

"""
Time Complexity: O(n) + O(n) + O(n) = O(3n) 
The time complexity of the above approach is O(N) because we traverse each consecutive subsequence only once.
Space Complexity: The space complexity of the above approach is O(N) because we are maintaining a HashSet.
"""