"""
https://leetcode.com/problems/permutation-sequence/
https://www.codingninjas.com/codestudio/problems/1112626?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website
"""
#if n is the number of elements in array, then it wil contain EXACTLY n! permutations
def kthPermutation(n, k):
    fact = 1
    numbers = []
    for i in range(1, n):
        fact = fact * i
        numbers.append(i)
    numbers.append(n)
    ans = ""
    k = k - 1
    while True:
        ans = ans + str(numbers[k // fact])
        numbers.pop(k // fact)
        if len(numbers) == 0:
            break

        k = k % fact
        fact = fact // len(numbers)
    return ans


for _ in range(int(input())):
    n, k = map(int, input().split())
    print(kthPermutation(n, k))
"""
Time Complexity: O(N) * O(N) = O(N^2)

Reason: We are placing N numbers in N positions. This will take O(N) time. For every number, we are reducing the search space by removing the element already placed in the previous step. This takes another O(N) time.

Space Complexity: O(N) 

Reason: We are storing  the numbers in a data structure(here vector)
"""