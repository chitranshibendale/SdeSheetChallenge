"""
https://takeuforward.org/data-structure/subset-sum-sum-of-all-subsets/
https://www.codingninjas.com/codestudio/problems/subset-sum_3843086?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website
https://practice.geeksforgeeks.org/problems/subset-sums2234/1
"""
# number of subsets = 2^n
def f(arr, i, sum, n, output):
    if i == n:
        output.append(sum)
        return
    f(arr, i + 1, sum + arr[i], n, output)
    f(arr, i + 1, sum, n, output)

def subsetSum(num):
    n = len(num)
    output = []
    f(num, 0, 0, n, output)
    return sorted(output)

for _ in range(int(input())):
    n = int(input())
    arr = [int(i) for i in input().split()]
    print(subsetSum(arr))
"""
Tc : 2^n + 2^n log(2^n)   #2^n log(2^n) : for sorting an array
Sc : 2^n
"""