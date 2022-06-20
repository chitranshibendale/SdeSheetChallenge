"""LEETCODE"""
class Solution:
    def f(self, s, dictionary, output, ans=""):
        if len(s) == 0:
            final = ans[:len(ans) - 1]
            output.append(final)
            return
        for i in range(len(s)):
            left = s[:i + 1]
            if left in dictionary:
                right = s[i + 1:]
                self.f(right, dictionary, output, ans + left + " ")

    def wordBreak(self, s, wordDict):
        output = []
        self.f(s, wordDict, output)
        return output