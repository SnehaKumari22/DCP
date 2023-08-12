"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Input: nums = [3,2,4], target = 6
Output: [1,2]
Input: nums = [3,3], target = 6
Output: [0,1]
"""


def twosum(nums):
	for i in range(len(nums)):
        remaining = nums[:i]+nums[i+1:]
        if target-nums[i] in remaining:
            return i,remaining.index(target-nums[i])+1
