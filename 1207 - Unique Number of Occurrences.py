"""
Leetcode Problem 1207 - Unique Number of Occurrences

Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.
"""

# class Solution:
#     def uniqueOccurrences(self, arr: List[int]) -> bool:
#         ref = {}

#         for i in range(len(arr)):
#             if arr[i] not in ref:
#                 ref[arr[i]] = 1
#             else:
#                 ref[arr[i]] += 1
        
#         ref_list = list(ref.values())
#         unique_set = set()
#         for i in range(len(ref_list)):
#             if ref_list[i] not in unique_set:
#                 unique_set.add(ref_list[i])
#             else:
#                 return False
#         return True

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        from collections import Counter

        elem_count = Counter(arr)
        elem_count = list(elem_count.values())
        ref = set()
        for i in range(len(elem_count)):
            if elem_count[i] in ref:
                return False
            else:
                ref.add(elem_count[i])
        return True
