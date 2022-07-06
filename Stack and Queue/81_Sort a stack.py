def sortedInsert(stack, num):
    if len(stack) == 0 or (not len(stack) == 0 and stack[-1] < num):
        stack.append(num)
        return
    n = stack[-1]
    stack.pop()
    sortedInsert(stack, num)
    stack.append(n)

def sortStack(stack):
    if len(stack) == 0:
        return
    num = stack[-1]
    stack.pop()
    sortStack(stack)
    sortedInsert(stack, num)
    # given data structure is a python list
    # as list have all the similar operations available so use them
    # Write your code here
