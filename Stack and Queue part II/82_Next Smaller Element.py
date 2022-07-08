#right
def nextSmallerElement(arr,n):
    stack = [-1]
    ans = []
    for i in range(n-1, -1, -1):
        item = arr[i]
        while stack[-1] >= item:
            stack.pop()
        ans.append(stack[-1])
        stack.append(item)
    return ans[::-1]