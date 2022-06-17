"""
https://takeuforward.org/data-structure/combination-sum-1/
https://leetcode.com/problems/combination-sum/
https://www.codingninjas.com/codestudio/problems/759331?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website
"""
def f1(ind, k, arr, n, output, ds): #leetcode
    if ind == n:
        if k == 0:
            output.append(ds.copy())
        return
    if arr[ind] <= k:
        ds.append(arr[ind])
        f1(ind, k - arr[ind], arr, n, output, ds)
        ds.pop()
    f1(ind + 1, k, arr, n, output, ds)

def f(ind, k, arr, n, output, ds):  #codestudio
    if ind == n:
        if k == 0:
            output.append(ds.copy())
        return
    ds.append(arr[ind])
    f(ind + 1, k - arr[ind], arr, n, output, ds)
    ds.pop()
    f(ind + 1, k, arr, n, output, ds)




def findSubsetsThatSumToK(arr, n, k) :
    output = []
    ds = []
    f(0, k, arr, n, output, ds)
    return output



n = int(input())
arr = [int(i) for i in input().split()]
k = int(input())
print(findSubsetsThatSumToK(arr, n, k))