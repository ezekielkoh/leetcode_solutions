"""
Leetcode 345 - Reverse Vowels of a String

Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

"""

class Solution:
    def reverseVowels(self, s: str) -> str:
        ref = set("aeiouAEIOU")
        vowels = [c for c in s if c in ref]
        result = []
        s = list(s)

        for i in range(len(s)):
            if s[i] in ref:
                result.append(vowels.pop())
            else:
                result.append(s[i])
        return "".join(result)
