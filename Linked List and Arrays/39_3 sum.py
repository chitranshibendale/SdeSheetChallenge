"""
https://leetcode.com/problems/3sum/
https://www.codingninjas.com/codestudio/problems/893028?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website
https://takeuforward.org/data-structure/3-sum-find-triplets-that-add-up-to-a-zero/
"""
"""
Time Complexity : O(n^2)  

Space Complexity : O(M).
"""
from sys import stdin, stdout
def threeSum(self, nums): #Leetcode
    nums.sort()
    ans = []
    for i in range(len(nums) - 2):
        if i == 0 or (i > 0 and nums[i] != nums[i - 1]):
            lo = i + 1
            hi = len(nums) - 1
            s = 0 - nums[i]
            while lo < hi:
                if nums[lo] + nums[hi] == s:
                    ans.append([nums[i], nums[lo], nums[hi]])
                    while lo < hi and nums[lo] == nums[lo + 1]:
                        lo += 1
                    while lo < hi and nums[hi] == nums[hi - 1]:
                        hi -= 1
                    lo += 1
                    hi -= 1
                else:
                    if nums[lo] + nums[hi] < s:
                        lo += 1
                    else:
                        hi -= 1
    return ans

def findTriplets(a, n, k): #codestudio
    a.sort()
    ans = []
    for i in range(n - 2):
        if (i == 0 or a[i] > a[i - 1]):
            start = i + 1
            end = n - 1
            target = k - a[i]
            while (start < end):
                if (start > i + 1 and
                        a[start] == a[start - 1]):
                    start += 1
                    continue
                if (end < n - 1 and
                        a[end] == a[end + 1]):
                    end -= 1
                    continue
                if (target == a[start] + a[end]):
                    ans.append([a[i], a[start], a[end]])
                    start += 1
                    end -= 1
                elif (target > (a[start] + a[end])):
                    start += 1
                else:
                    end -= 1
    return ans



# Taking input using fast I/0.
def takeInput():
    N = int(stdin.readline())
    arr = list(map(int, stdin.readline().strip().split(" ")))
    K = int(stdin.readline())
    return N, arr, K


tc = int(input())
while tc > 0:
    N, arr, K = takeInput()
    ans = findTriplets(arr, N, K)

    if len(ans) == 0:
        stdout.write("-1\n")

    else:
        for i in ans:
            i.sort()
            stdout.write(str(i[0]) + " " + str(i[1]) + " " + str(i[2]) + "\n")

    tc -= 1
