"""
https://takeuforward.org/data-structure/print-all-permutations-of-a-string-array/
https://www.codingninjas.com/codestudio/problems/758958?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website
https://leetcode.com/problems/permutations/
"""


def f(ind, s, ans, temp):
    if ind >= len(s):
        x = ""
        for i in temp:
            x += i
        ans.append(x)
        return
    for i in range(ind, len(s)):
        temp[ind], temp[i] = temp[i], temp[ind]
        f(ind + 1, s, ans, temp)
        temp[ind], temp[i] = temp[i], temp[ind]


def findPermutations(s):
    ans = []
    temp = list(s)
    f(0, s, ans, temp)
    return ans


s = input()
print(findPermutations(s))