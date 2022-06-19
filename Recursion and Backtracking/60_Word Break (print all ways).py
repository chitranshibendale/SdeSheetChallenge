"""
https://www.codingninjas.com/codestudio/problems/983635?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website
https://www.youtube.com/watch?v=LmHWIsBQBU4
"""
def f(s, dictionary, output, ans=""):
    if len(s) == 0:
        output.append(ans)
        return
    for i in range(len(s)):
        left = s[:i+1]
        if left in dictionary:
            right = s[i+1:]
            f(right, dictionary, output, ans + left + " ")
def wordBreak(s, dictionary):
    output = []
    f(s, dictionary, output)
    return output
