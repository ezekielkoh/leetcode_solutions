"""
Leetcode Problem 392 - Is Subsequence

Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
"""

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        p1 = 0
        p2 = 0

        s = list(s)
        t = list(t)

        while p1 < len(s) and p2 < len(t):
            if s[p1] == t[p2]:
                p1 += 1
                if p1 >= len(s):
                    return True
            p2 += 1
        if not s:
            return True
        return False