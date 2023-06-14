"""
Leetcode Problem 242: Valid Anagram

Parses 2 string into isAnagram function. Returns true if the 2 strings are anagrams of each other.
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # returns False since length of both strings are not equal
        if len(s) != len(t):
            return False
        
        # sorts both strings and compares each character
        sorted_s = sorted(s)
        sorted_t = sorted(t)

        for i in range(len(s)):
            if sorted_s[i] != sorted_t[i]:
                return False
        
        return True
