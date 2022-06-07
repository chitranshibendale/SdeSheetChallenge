""""
https://www.youtube.com/watch?v=hVl2b3bLzBw&list=PLgUwDviBIf0rPG3Ictpu74YWBQ1CaBkm2&index=5&ab_channel=takeUforward
https://www.codingninjas.com/codestudio/problems/1214628?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website
https://leetcode.com/problems/merge-sorted-array/
"""


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        tmp_nums1 = nums1[:m]

        p1 = 0
        p2 = 0

        for p in range(n + m):

            if p2 >= n or (p1 < m and tmp_nums1[p1] <= nums2[p2]):
                nums1[p] = tmp_nums1[p1]
                p1 += 1
            else:
                nums1[p] = nums2[p2]
                p2 += 1