"""
https://takeuforward.org/data-structure/count-maximum-consecutive-ones-in-the-array/
https://leetcode.com/problems/max-consecutive-ones/
https://www.youtube.com/watch?v=Mo33MjjMlyA&list=PLgUwDviBIf0p4ozDR_kJJkONnb1wdx2Ma&index=44&ab_channel=takeUforward
"""
def findMaxConsecutiveOnes(nums):
    count = 0
    maxi = 0
    for i in nums:
        if i == 1:
            count += 1
        else:
            count = 0
        maxi = max(maxi, count)
    return maxi