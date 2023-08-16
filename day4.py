"""
Given an unsorted integer array nums, return the smallest missing positive integer.

You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.
Input: nums = [1,2,0]
Output: 3
Input: nums = [3,4,-1,1]
Output: 2
Input: nums = [7,8,9,11,12]
Output: 1
[1,1]->2

"""

def sol1(nums):
	l = [0]*len(nums)
    for i in nums:
        if i>0:
            if i>len(nums):
                pass
            else:
                l[i-1]=1
    for i in range(len(l)):
        if l[i]==0:
            return i+1
    return len(nums)+1

def cyclesort_sol(nums):
	i=0
    while(i<len(nums)):
        c=nums[i]-1
        if(nums[i]<=len(nums) and nums[i]>0 and nums[i]!=nums[c]):
            nums[i],nums[c]=nums[c],nums[i]
        else:
            i+=1
    for i in range(len(nums)):
        if nums[i]!=i+1:
            return i+1
    return len(nums)+1