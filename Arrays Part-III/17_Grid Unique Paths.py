"""
https://www.youtube.com/watch?v=t_f0nwwdg5o&ab_channel=takeUforward
https://takeuforward.org/data-structure/grid-unique-paths-count-paths-from-left-top-to-the-right-bottom-of-a-matrix/
https://www.codingninjas.com/codestudio/problems/1081470?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website
https://leetcode.com/problems/unique-paths/
"""


def uniquePaths(m, n):
    N = n + m - 2 # total directions
    r = m - 1
    res = 1
    for i in range(1, r + 1):
        res = res * (N - r + i) // i
    return res



for _ in range(int(input())):
    m, n = map(int, input().split())
    print(uniquePaths(m, n))

    """
    TC : O(m - 1)
    SC : O(1)
    """