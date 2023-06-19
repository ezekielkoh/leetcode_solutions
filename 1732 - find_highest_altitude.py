""" 
Leetcode Problem 1732 - Find Highest Altitude

There is a biker going on a road trip. The road trip consists of n + 1 points at different altitudes. The biker starts his trip on point 0 with altitude equal 0.
You are given an integer array gain of length n where gain[i] is the net gain in altitude between points i​​​​​​ and i + 1 for all (0 <= i < n). Return the highest altitude of a point.

Solution is done by updating the max_gain variable if the current gain is greater than the max_gain.
"""


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_gain = 0
        curr_gain = 0
        for i in range(len(gain)):
            curr_gain += gain[i]
            if curr_gain > max_gain:
                max_gain = curr_gain
        return max_gain