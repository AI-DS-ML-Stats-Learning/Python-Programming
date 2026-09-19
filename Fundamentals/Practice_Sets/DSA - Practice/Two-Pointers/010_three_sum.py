# Problem Description
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
# such that:

# i != j, i != k, and j != k (all three indices are distinct)
# nums[i] + nums[j] + nums[k] == 0
# Crucial Rule: The solution set must not contain duplicate triplets.

# Examples
# Example 1:
# Input: nums = [-1, 0, 1, 2, -1, -4]
# Output: [[-1, -1, 2], [-1, 0, 1]]
# (Notice: nums has two -1s, but we don't return duplicate triplets).
# Example 2:
# Input: nums = [0, 1, 1]
# Output: []
# Example 3:
# Input: nums = [0, 0, 0]
# Output: [[0, 0, 0]]

nums = [-1, 0, 1, 2, -1, -4]

def three_sum(nums) -> list:
    result = []
    for i in range(len(nums)):
        l = i+1
        r = len(nums) -1
        if i > 0 and nums[i] == nums[i-1]:
            continue

        while l < r:
            three_sum = nums[i] + nums[l] + nums[r]

            if three_sum > 0:
                r -= 1
            elif three_sum < 0:
                l += 1
            else:
                result.append([nums[i], nums[l], nums[r]])

                l += 1
                while l<r and nums[l] == nums[l-1]:
                    l+=1


    return result


print(three_sum(sorted(nums)))

