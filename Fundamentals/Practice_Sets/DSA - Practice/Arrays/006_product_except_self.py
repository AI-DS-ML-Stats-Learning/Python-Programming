# Problem Description
# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# Constraints:

# You must write an algorithm that runs in O(N) time.
# You cannot use the division division operator /!
# Examples
# Example 1:
# Input: nums = [1, 2, 3, 4]
# Output: [24, 12, 8, 6]
# (Explanation: 24 = 2*3*4, 12 = 1*3*4, 8 = 1*2*4, 6 = 1*2*3)
# Example 2:
# Input: nums = [-1, 1, 0, -3, 3]
# Output: [0, 0, 9, 0, 0]

nums = [1, 2, 3, 4]

prefix_Arr = []
suffix_Arr = []
def product_except_self(nums):
    '''calculating prefix'''
    j = 1
    for i in nums:
        j = j*i
        prefix_Arr.append(j)

    print(prefix_Arr)

    '''calculating suffix'''
    j = 1
    for i in nums[::-1]:
        j = j*i
        suffix_Arr.append(j)

    print(suffix_Arr)

product_except_self(nums)
