"""
Leetcode Problem 283 - Move Zeroes

Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the
"""

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            if nums[i] == 0:
                nums.remove(nums[i])
                nums.append(0)