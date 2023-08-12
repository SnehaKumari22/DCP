"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
No division
Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
"""

##### With Division #########
def sol_with_div(nums):
	res = []
    m=1
    flag = 0
    idx =[]
    for i in range(len(nums)):
        if nums[i] == 0:
            flag+= 1
            idx.append(i)
        else:
            m=m*nums[i]
    if flag ==1:
        res=[0]*len(nums)
        res[idx[0]]=m
    elif flag> 1:
        res=[0]*len(nums)
    else:
        for i in nums:
            res.append(m//i)
    return res

##### Without division  2 array #####
def sol_2_arr(nums):
	arr1,arr2 = [],[]
    res =[]
    start,end=1,1
    for i in range(len(nums)):
        arr1.append(start)
        start= start*nums[i]
    for i in range(len(nums)-1,-1,-1):
        arr2.append(end)
        end= end*nums[i]
    for i in range(len(nums)):
        res.append(arr1[i]*arr2[len(nums)-i-1])
    return res



##### Without Division #####
def sol_wo_div(nums):
	n =len(nums)
    res=[1]*n
    s,e=1,1
    for i in range(n):
        res[i]= res[i]*s
        s=s*nums[i]
        res[n-i-1]=res[n-i-1]*e
        e=e*nums[n-i-1]
        print(res,nums[i],s,e,nums[n-i-1])
    return res