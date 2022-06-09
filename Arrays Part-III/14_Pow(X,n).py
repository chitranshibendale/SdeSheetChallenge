"""
https://www.youtube.com/watch?v=l0YC3876qxg&list=PLgUwDviBIf0rPG3Ictpu74YWBQ1CaBkm2&index=16&ab_channel=takeUforward
https://takeuforward.org/data-structure/implement-powxn-x-raised-to-the-power-n/
https://leetcode.com/problems/powx-n/
https://www.codingninjas.com/codestudio/problems/1082146?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website
"""
import sys
sys.setrecursionlimit(10**7)

def modularExponentiation(x, n, m):
    if n == 0:
        return 1
    smallPower = modularExponentiation(x, n // 2, m)
    if n % 2 == 0:
        return (smallPower * smallPower)% m
    else:
        return (x * smallPower * smallPower) % m


t = int(input())
while (t > 0):
    lst = list(map(int,input().split()))
    x,n,m = lst[0], lst[1], lst[2]
    print(modularExponentiation(x, n, m) % m)
    t -= 1

"""
TC and Sc : O(log n)
"""