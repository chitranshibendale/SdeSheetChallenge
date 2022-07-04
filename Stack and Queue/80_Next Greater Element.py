from sys import stdin


def nextGreater(arr, n):
    stack = []
    ans = [-1]*n
    for i in range(2*n - 1, -1, -1):
        while stack and stack[-1] <= arr[i%n]:
            stack.pop()
        if i < n:
            if stack:
                ans[i] = stack[-1]
            else:
                ans[i] = -1
        stack.append(arr[i%n])
    return ans


# Your code goes here


# Main

t = int(stdin.readline().rstrip())

while t > 0:

    n = int(stdin.readline().rstrip())
    arr = list(map(int, stdin.readline().rstrip().split(" ")))
    z = (nextGreater(arr, n))
    for i in z:
        print(i, end=" ")
    print()

    t -= 1
