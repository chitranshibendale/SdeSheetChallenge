"""
https://takeuforward.org/data-structure/length-of-longest-substring-without-any-repeating-character/
https://www.youtube.com/watch?v=qtVh-XEpsJo&list=PLgUwDviBIf0p4ozDR_kJJkONnb1wdx2Ma&index=27&ab_channel=takeUforward
https://leetcode.com/problems/longest-substring-without-repeating-characters/
https://www.codingninjas.com/codestudio/problems/630418?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website
"""
def uniqueSubstrings(input):
    d = {}
    maxi = 0
    start = 0
    for end in range(len(input)):
        if input[end] in d:
            start = max(start, d[input[end]] + 1)
        d[input[end]] = end
        maxi = max(maxi, end - start + 1)
    return maxi

s = input()
print(uniqueSubstrings(s))
"""
TC, SC : O(n)
"""