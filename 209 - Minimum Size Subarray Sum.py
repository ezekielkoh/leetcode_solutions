"""
Leetcode Problem 209 - Find Minimum Size Subarray Sum
"""

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0

        minLen = float('inf')
        p1 = 0
        total = 0

        for i in range(len(nums)):
            total += nums[i]
            while total >= target:
                minLen = min(minLen, i-p1+1)
                total -= nums[p1]
                p1 += 1
        return minLen