"""
https://leetcode.com/problems/subsets-ii/
https://www.codingninjas.com/codestudio/problems/unique-subsets_3625236?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website
https://takeuforward.org/data-structure/subset-ii-print-all-the-unique-subsets/
"""
def f(arr, n, ind, temp, output):
    output.append(temp.copy())
    for i in range(ind, n):
        if i != ind and arr[i] == arr[i-1]:
            continue
        temp.append(arr[i])
        f(arr, n, i + 1, temp, output)
        temp.pop()



def uniqueSubsets(n,arr):
    output = []
    ds = []
    arr.sort()
    f(arr, n, 0, ds, output)
    return output

for _ in range(int(input())):
    n = int(input())
    arr = [int(i) for i in input().split()]
    print(uniqueSubsets(n, arr))

"""
Time Complexity: O(2^n) for generating every subset and O(k)  to insert every subset in another data structure if the average length of every subset is k. Overall O(k * 2^n).

Space Complexity: O(2^n * k) to store every subset of average length k. Auxiliary space is O(n)  if n is the depth of the recursion tree.
"""