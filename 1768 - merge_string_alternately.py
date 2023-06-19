"""
Leetcode Problem - 1768

You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.
Return the merged string.

Solution is done using a while loop to iteratively pop the first character of each string and stores in a new string.
"""

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = []
        word1 = [x for x in word1]
        word2 = [x for x in word2]
        while word1 and word2:
            merged.append(word1.pop(0))
            merged.append(word2.pop(0))
        while word1:
            merged.append(word1.pop(0))
        while word2:
            merged.append(word2.pop(0))
        return ''.join(merged)