def isValidParenthesis(expression):
    s = []
    for i in expression:
        if i in '({[':
            s.append(i)
        elif i == ')':
            if not s or s[-1] != '(':
                return False
            s.pop()
        elif i == '}':
            if not s or s[-1] != '{':
                return False
            s.pop()
        elif i == ']':
            if not s or s[-1] != '[':
                return False
            s.pop()
    if s:
        return False
    return True


# Main Code

t = int(input().strip())

for i in range(t):
    str = input().strip()
    ans = isValidParenthesis(str)

    if ans:
        print("Balanced")

    else:
        print("Not Balanced")
