"""
https://takeuforward.org/data-structure/job-sequencing-problem/
https://www.codingninjas.com/codestudio/problems/job-sequencing-problem_1169460?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website
https://practice.geeksforgeeks.org/problems/job-sequencing-problem-1587115620/1#
"""
def jobScheduling(jobs):
    n = len(jobs)
    jobs.sort(reverse=True, key=lambda x: x[1])
    maxDeadline = jobs[0][0]
    for i in range(1, n):
        maxDeadline = max(maxDeadline, jobs[i][0])
    slot = [-1] * (maxDeadline + 1)
    countJob, jobProfit = 0, 0

    for i in range(n):
        for j in range(jobs[i][0], 0, -1):
            if slot[j] == -1:
                slot[j] = i
                countJob += 1
                jobProfit += jobs[i][1]
                break
    return jobProfit
"""
Time Complexity: O(N log N) + O(N*M).

O(N log N ) for sorting the jobs in decreasing order of profit. O(N*M) since we are iterating through all N jobs and for every job we are checking from the last deadline, say M deadlines in the worst case.

Space Complexity: O(M) for an array that keeps track on which day which job is performed if M is the maximum deadline available.
"""