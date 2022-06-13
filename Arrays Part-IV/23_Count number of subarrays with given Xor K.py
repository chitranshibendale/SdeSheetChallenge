"""
https://takeuforward.org/data-structure/count-the-number-of-subarrays-with-given-xor-k/
https://www.youtube.com/watch?v=lO9R5CaGRPY&list=PLgUwDviBIf0p4ozDR_kJJkONnb1wdx2Ma&index=26&ab_channel=takeUforward
https://www.interviewbit.com/problems/subarray-with-given-xor/
https://www.codingninjas.com/codestudio/problems/1115652?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website
"""
def subarraysXor(arr, x):
    d = {}
    xor = 0
    count = 0
    n = len(arr)
    for i in range(n):
        xor ^= arr[i]
        y = xor ^ x
        if y in d:
            count += d[y]
        if xor == x:
            count += 1
        if xor in d:
            d[xor] += 1
        else:
            d[xor] = 1
    return count

for _ in range(int(input())):
    n, x = map(int, input().split())
    arr = [int(i) for i in input().split()]
    print(subarraysXor(arr, x))
"""
Time Complexity: O(n)

Space Complexity: O(n)
"""