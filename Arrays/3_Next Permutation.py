"""
https://takeuforward.org/data-structure/next_permutation-find-next-lexicographically-greater-permutation/
https://www.youtube.com/watch?v=LuLCLgMElus&list=PLgUwDviBIf0rPG3Ictpu74YWBQ1CaBkm2&index=10&ab_channel=takeUforward
https://www.codingninjas.com/codestudio/problems/893046?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website
https://leetcode.com/problems/next-permutation/
"""

def swapElements(arr, start, end) :
    arr[start], arr[end] = arr[end], arr[start]


def reverse(arr, start, end):
    while(start < end):
        swapElements(arr, start, end)
        start += 1
        end -= 1

def nextPermutation(permutation, n):
    k = n - 2
    while k >= 0:
        if permutation[k] < permutation[k+1]:
            break
        k -= 1
    if k < 0:
        permutation.reverse()
    else:
        l = n - 1
        while l > k:
            if permutation[l] > permutation[k]:
                break
            l -= 1
        permutation[k], permutation[l] = permutation[l], permutation[k]
        reverse(permutation, k+1, n-1)







for _ in range(int(input())):
    n = int(input())
    arr = [int(i) for i in input().split()]
    nextPermutation(arr, n)
    print(arr)

#Tc : O(n) + O(n) + O(n) = O(n)
#SC = O(1)