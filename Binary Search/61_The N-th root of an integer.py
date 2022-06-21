"""
https://takeuforward.org/data-structure/nth-root-of-a-number-using-binary-search/
https://www.codingninjas.com/codestudio/problems/1062679?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website
"""
def multiply(number, n):
    ans = 1
    for i in range(1, n+1):
        ans = ans * number
    return ans

def findNthRootOfM(n,m):
    low = 1
    high = m
    eps = 1e-6
    while (high - low) > eps:
        mid = (low + high) / 2
        if multiply(mid, n) < m:
            low = mid
        else:
            high = mid

    return low

for _ in range(int(input())):
    n, m = map(int, input().split())
    print(findNthRootOfM(n, m))