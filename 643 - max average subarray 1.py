"""
Leetcode Problem 643 - Maximum Average Subarray I

Given an array consisting of n integers, find the contiguous subarray of given length k that has the maximum average
"""

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        p1 = 0
        p2 = k

        currSum = sum(nums[p1:p2])
        maxSum = currSum

        while p2 < len(nums):
            currSum = currSum - nums[p1] + nums[p2]
            if currSum > maxSum:
                maxSum = currSum
            p1 += 1
            p2 += 1
        
        return maxSum / k