"""
https://takeuforward.org/data-structure/combination-sum-ii-find-all-unique-combinations/
https://leetcode.com/problems/combination-sum-ii/
https://www.codingninjas.com/codestudio/problems/1112622?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website
"""


def f(ind, sum, temp, target, n, arr, ans):
    if sum == target:
        ans.append(temp[:])
        return
    if ind == n or sum > target:
        return
    for i in range(ind, n):
        if i > ind and arr[i] == arr[i - 1]:
            continue
        temp.append(arr[i])
        f(i + 1, sum + arr[i], temp, target, n, arr, ans)
        temp.pop()


def combinationSum2(arr, n, target):
    arr.sort()
    ans = []
    f(0, 0, [], target, n, arr, ans)
    return ans


for _ in range(int(input())):
    n, target = map(int, input().split())
    arr = [int(i) for i in input().split()]
    print(combinationSum2(arr, n, target))