"""
https://leetcode.com/problems/palindrome-partitioning/
https://www.codingninjas.com/codestudio/problems/799931?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website
https://takeuforward.org/data-structure/palindrome-partitioning/
"""
from sys import stdin
import json
def isPalindrome(s, start, end):
    if start >= end:
        return True
    if s[start] != s[end]:
        return False
    return isPalindrome(s, start + 1, end - 1)

def f(ind, s, path, ans):
    if ind == len(s):
        ans.append(path.copy())
        return
    for i in range(ind, len(s)):
        if isPalindrome(s, ind, i):

            path.append(s[ind : i + 1])
            f(i + 1, s, path, ans)
            path.pop()


def partition(s):
    ans = []
    path = []
    f(0, s, path, ans)
    return ans


s=stdin.readline().rstrip()

final=partition(s)

for ele in final:
    ele = sorted(ele)
    print(json.dumps(ele))

"""
Time Complexity: O( (2^n) *k*(n/2) )

Reason: O(2^n) to generate every substring and O(n/2)  to check if the substring generated is a palindrome. O(k) is for inserting the palindromes in another data structure, where k  is the average length of the palindrome list.

Space Complexity: O(k * x)

Reason: The space complexity can vary depending upon the length of the answer. k is the average length of the list of palindromes and if we have x such list of palindromes in our final answer. The depth of the recursion tree is n, so the auxiliary space required is equal to the O(n).
"""
