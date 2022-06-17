"""
https://practice.geeksforgeeks.org/problems/n-meetings-in-one-room-1587115620/1
https://www.codingninjas.com/codestudio/problems/1062712?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website
https://takeuforward.org/data-structure/n-meetings-in-one-room/
"""
"""
Overall : O(n) +O(n log n) + O(n) ~O(n log n)

Space Complexity: O(n)  since we used an additional data structure for storing the start time, end time, and meeting no.
"""
def maximumActivities(start, end):
    n = len(start)
    meet = []
    for i in range(n):
        meet.append([start[i], end[i], i + 1])
    meet.sort(key = lambda x:x[1])
    answer = 1
    limit = meet[0][1]
    for i in range(1, n):
        if meet[i][0] >= limit:
            limit = meet[i][1]
            answer += 1
    return answer

for _ in range(int(input())):
    n = int(input())
    arr = [int(i) for i in input().split()]
    arr2 = [int(i) for i in input().split()]
    print(maximumActivities(arr, arr2))