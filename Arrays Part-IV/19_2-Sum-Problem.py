"""
https://takeuforward.org/data-structure/two-sum-check-if-a-pair-with-given-sum-exists-in-array/
https://www.youtube.com/watch?v=dRUpbt8vHpo&list=PLgUwDviBIf0rVwua0kKYlsS_ik_1lyVK_&index=2&ab_channel=takeUforward
https://www.codingninjas.com/codestudio/problems/pair-sum_697295?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website
https://leetcode.com/problems/two-sum/
"""
def pairSum1(arr, s):
    # Leetcode
    d = {}
    ans = []
    for i in range(len(arr)):
        if s - arr[i] in d:
            ans.append(d[s - arr[i]])
            ans.append(i)
            return ans
        d[arr[i]] = i
    return ans

def helper(arr, n, num) :
    if n == 0:
        return 0
    arr.sort()
    countDigit = {}
    ans = []
    for i in arr:
        countDigit[i] = countDigit.get(i, 0) + 1
    i = 0
    j = n-1
    while (i<=j):
        sum = arr[i] + arr[j]
        if sum == num:
            count = 0
            if arr[i] == arr[j]:
                count += ((countDigit[arr[j]]) * (countDigit[arr[j]]-1))//2
                for _ in range(count):
                    ans.append(tuple((arr[i], arr[j])))
            else:
                count += countDigit[arr[i]] * countDigit[arr[j]]
                for _ in range(count):
                    ans.append(tuple((arr[i], arr[j])))
            i+=countDigit[arr[i]]
            j-=countDigit[arr[j]]
        elif sum > num:
            j-=countDigit[arr[j]]
        else:
            i+=countDigit[arr[i]]
    return ans


def pairSum(arr, s):
    return helper(arr, len(arr), s)


n, s = map(int, input().split())
arr = [int(i) for i in input().split()]
print(pairSum(arr, s))
"""
Time Complexity: O(N)

Space Complexity: O(N)
"""