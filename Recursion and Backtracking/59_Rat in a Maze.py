"""
https://practice.geeksforgeeks.org/problems/rat-in-a-maze-problem/1
https://www.codingninjas.com/codestudio/problems/758966?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website
https://takeuforward.org/data-structure/rat-in-a-maze/
"""
#GFG
def solve(i, j, maze, n, ans, move, visit):
    if i == n - 1 and j == n - 1:
        ans.append(move)
        return
    if i + 1 < n and not visit[i+1][j] and maze[i+1][j] == 1:
        visit[i][j] = 1
        solve(i+1, j, maze, n, ans, move + "D", visit)
        visit[i][j] = 0
    if j - 1 >= 0 and not visit[i][j-1] and maze[i][j-1] == 1:
        visit[i][j] = 1
        solve(i, j-1, maze, n, ans, move + "L", visit)
        visit[i][j] = 0
    if j + 1 < n and not visit[i][j+1] and maze[i][j+1] == 1:
        visit[i][j] = 1
        solve(i, j+1, maze, n, ans, move + "R", visit)
        visit[i][j] = 0
    if i - 1 >= 0 and not visit[i-1][j] and maze[i - 1][j] == 1:
        visit[i][j] = 1
        solve(i-1, j, maze, n, ans, move + "U", visit)
        visit[i][j] = 0

def ratInAMaze(maze, n):
    ans = []
    visit = [[0 for j in range(n)] for i in range(n)]
    if maze[0][0] == 1:
        solve(0, 0, maze, n, ans, "", visit)
    return ans


# Main.
n = int(input())
maze = n * [0]

for i in range(0, n):
    maze[i] = input().split()
    maze[i] = [int(j) for j in maze[i]]

print(ratInAMaze(maze, n))
# print(maze)
"""
4
1 0 0 0
1 1 0 1
1 1 0 0
0 1 1 1
"""