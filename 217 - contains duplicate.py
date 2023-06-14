"""
Leetcode Problem 217: Contains Duplicate

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
Input: containsDuplicate(nums) where nums is a list of integers
Output: boolean

Duplicated values are added into a set. If a value is already in the set, return True. If the loop ends, return False.
"""

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        sorted_nums = sorted(nums)
        ref = set()
        for i in range(len(sorted_nums)):
            if sorted_nums[i] in ref:
                return True
            else:
                ref.add(sorted_nums[i])
        return False
