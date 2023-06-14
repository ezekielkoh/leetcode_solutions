"""
Leetcode Problem 20: Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
"""


class Solution:
    def isValid(self, s: str) -> bool:
        # create dictionary for reference
        ref = dict(('()', '{}', '[]'))

        # create LIFO stack 
        stack = []

        # verify and add closing bracket to stack
        for char in s:
            if char in ref.keys():
                temp = ref[char]
                stack.append(temp)
            else:
                if len(stack) == 0:
                    return False
                else:
                    if char != stack.pop():
                        return False
                        
        # stack should be empty if brackets are closed correctly
        return len(stack) == 0


