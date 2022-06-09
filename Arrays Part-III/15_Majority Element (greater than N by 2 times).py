"""
https://www.youtube.com/watch?v=AoX3BPWNnoE&list=PLgUwDviBIf0rPG3Ictpu74YWBQ1CaBkm2&index=17&ab_channel=takeUforward
https://www.codingninjas.com/codestudio/problems/1082146?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website
https://leetcode.com/problems/powx-n/
https://www.youtube.com/watch?v=7pnhv842keE&ab_channel=NeetCode
"""

# Moore Algorithm

def findMajorityElement(arr, n):
    result, count = 0, 0
    for ele in arr:
        if count == 0:
            result = ele
        if ele == result:
            count += 1
        else:
            count -= 1
    return result

for _ in range(int(input())):
    n = int(input())
    arr = [int(i) for i in input().split()]
    print(findMajorityElement(arr, n))

#TC : O(n)
#SC : O(1)