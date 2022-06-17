""""
https://takeuforward.org/data-structure/n-meetings-in-one-room/
https://www.codingninjas.com/codestudio/problems/1062658?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website
https://practice.geeksforgeeks.org/problems/n-meetings-in-one-room-1587115620/1
"""
def maximumMeetings(start, end):
    n = len(start)
    meet = []
    for i in range(n):
        meet.append([start[i], end[i], i + 1])
    meet.sort(key = lambda x:x[1])
    answer = []
    limit = meet[0][1]
    answer.append(meet[0][2])
    for i in range(n):
        if meet[i][0] > limit:
            limit = meet[i][1]
            answer.append(meet[i][2])
    return answer






for _ in range(int(input())):
    n = int(input())
    arr = [int(i) for i in input().split()]
    arr2 = [int(i) for i in input().split()]
    print(maximumMeetings(arr, arr2))
    """
    Time Complexity: O(n) to iterate through every position and insert them in a data structure. O(n log n)  to sort the data structure in ascending order of end time. O(n)  to iterate through the positions and check which meeting can be performed.

Overall : O(n) +O(n log n) + O(n) ~O(n log n)

Space Complexity: O(n)  since we used an additional data structure for storing the start time, end time, and meeting no.
    """