# Problem Description
# Given an integer array nums, return an array answer such that answer[i] is equal to 
# the product of all the elements of nums except nums[i].

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

# nums = [2, 2, 3, 4, 5, 6]
nums = [1, 2, 3, 4]

prefix_Arr = []
suffix_Arr = []
prod_arr = []
def product_except_self(nums):
    '''calculating prefix'''
    j = 1
    for i in nums:
        j = j*i
        prefix_Arr.append(j)

    prefix_Arr.pop() #alternative to prefix_Arr[:len(prefix_Arr)-1]
    # print(prefix_Arr)

    '''calculating suffix'''
    j = 1
    for i in nums[::-1]:
        j = j*i
        suffix_Arr.append(j)

    suffix_Arr.pop() #alternative to prefix_Arr[:len(prefix_Arr)-1]
    # print(suffix_Arr)

    print(len(suffix_Arr))
    suf_len = len(suffix_Arr)
    
    prod_arr.append(suffix_Arr[-1]) #first element done
    for i in range(1, len(nums)-1):
        # print(i)
        prod_arr.append(prefix_Arr[i-1]*suffix_Arr[(i - (suf_len-1))*-1])

    prod_arr.append(prefix_Arr[-1])
    print(prod_arr)

product_except_self(nums)

"""optimized version"""

def product_except_self_optimized(nums):
    res = [1] * len(nums)  # Output list
    
    # 1. First pass: Calculate prefix products
    prefix = 1
    for i in range(len(nums)):
        res[i] = prefix
        prefix *= nums[i]
        
    # At this point, res = [1, 1, 2, 6]
    
    # 2. Second pass: Calculate postfix and multiply in-place
    postfix = 1
    for i in range(len(nums) - 1, -1, -1):  # Loop backwards
        res[i] *= postfix
        postfix *= nums[i]
        
    return res

print(product_except_self_optimized([1, 2, 3, 4]))
# Output: [24, 12, 8, 6]