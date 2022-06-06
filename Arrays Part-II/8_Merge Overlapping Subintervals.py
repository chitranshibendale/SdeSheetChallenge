"""
https://takeuforward.org/data-structure/merge-overlapping-sub-intervals/
https://www.youtube.com/watch?v=2JzRBPFYbKE&list=PLgUwDviBIf0rPG3Ictpu74YWBQ1CaBkm2&index=7&ab_channel=takeUforward
https://www.codingninjas.com/codestudio/problems/699917?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website
https://leetcode.com/problems/merge-intervals/
"""
######LEETCODE###################
def mergeIntervals(intervals):
    print(intervals)
    intervals.sort(key = lambda i : i[0])
    output = [intervals[0]]
    for start, end in intervals[1:]:
        lastEnd = output[-1][1]
        if start <= lastEnd:
            output[-1][1] = max(lastEnd, end)
        else:
            output.append([start, end])
    return output
###########CODESTUDIO#################
from sys import stdin, setrecursionlimit


class Solution:
    def __init__(self, start, end):
        self.start = start
        self.end = end


def mergeIntervals(intervals):
    # Write your code here.
    n = len(intervals)
    x = intervals[0].start
    y = intervals[0].end
    output = []
    for i in range(1, n):
        if intervals[i].start <= y:
            y = max(y, intervals[i].end)
        else:
            output.append(Solution(x, y))
            x = intervals[i].start
            y = intervals[i].end
    output.append(Solution(x, y))
    return output


n = int(input())
arr1 = list(map(int, stdin.readline().strip().split(" ")))
arr2 = list(map(int, stdin.readline().strip().split(" ")))
arr1.sort()
arr2.sort()
intervals = []
for i in range(n):
    a = Solution(arr1[i], arr2[i])
    intervals.append(a)

res = mergeIntervals(intervals)

for i in range(len(res)):
    print(res[i].start, res[i].end)




