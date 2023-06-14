"""
Leetcode Problem 53: Maximum Subarray

Given an integer array nums, find the subarray with the largest sum, and return its sum.

Uses Kadane's algorithm to find the maximum subarray sum.
"""


class Solution:
    def maxSubArray(self, nums) -> int:
        
        maxSum = float('-inf')  # set initial maxSum to the lowest possible value
        currSum = 0

        for i in range(len(nums)):
            currSum += nums[i]  
            # if current pointer in nums list is higher than cumulative value, set currSum to current pointer
            if currSum < nums[i]:   
                currSum = nums[i]
            # check again if currSum is higher than highest cumulative sum achieved so far
            if currSum > maxSum:
                maxSum = currSum

        return maxSum

