# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice. 
# You can return the answer in any order.

# Examples
# Example 1:
# Input: nums = [2, 7, 11, 15], target = 9
# Output: [0, 1] (because nums[0] + nums[1] == 9)
# Example 2:
# Input: nums = [3, 2, 4], target = 6
# Output: [1, 2] (because nums[1] + nums[2] == 6)

# Your Task:
# Brute Force: If you used nested loops (checking every possible pair of numbers), what would the Time Complexity be?
# The Math Hint: As you loop through the list, if the current number is x, the number you are looking for (the complement) is: 
# complement = target - x
# Write a Python function two_sum(nums, target) using a Dictionary (Hash Map) to solve this in 
# O(N) time and O(N) space.
# Hint: Store the numbers you have already visited and their indices in the dictionary: {number: index}.

nums = [2, 7, 11, 15]
target = 9

'''Brute Force:
Time Complexity - O(N^2)
'''
# indices = []

# for idx, i in enumerate(nums, start=1):
#     if i < target:
#         for jdx, j in enumerate(nums[idx:], start=idx+1):
#             # print(nums[idx:])
#             sum_var = 0
#             if j < target:
#                 sum_var = i+j
#                 # print(sum_var)
#                 indices = [idx, jdx]

#             if sum_var == target:
#                 print(indices)
#                 break

'''Hash Map'''
def two_sum(nums, target):

    prev_complement = {}

    for idx, i in enumerate(nums, start=1):
        comp =  target -  i

        if comp in prev_complement:
            print( [prev_complement[comp], idx])

        prev_complement[i] = idx

two_sum(nums, target)

