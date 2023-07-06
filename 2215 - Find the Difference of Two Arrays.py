"""
Leetcode Problem 2215 - Find the Difference of Two Arrays

Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:

answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
answer[1] is a list of all distinct integers in nums2 which are not present in nums1.

Solution is derieved by subtracting elements of nums1 from nums2 and vice versa.
Subsequently, the results arising from using the set function is converted back to a list
"""



class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        res1 = set(nums1) - set(nums2)
        res2 = set(nums2) - set(nums1)

        p1 = list(res1)
        p2 = list(res2)

        return [p1,p2]


