# Problem 7: Longest Consecutive Sequence
# LeetCode Link: #128 - Longest Consecutive Sequence
# Recommended Filename: 007_longest_consecutive.py
# Category: Arrays & Hashing
# Difficulty: Medium
# Problem Description
# Given an unsorted array of integers nums, return the length of the longest 
# consecutive elements sequence (e.g. [1, 2, 3, 4] is a consecutive sequence of length 4).

# Constraint: You must write an algorithm that runs in O(N) time. 
# (This means sorting is banned, because sorting takes O(NlogN)!).

# Examples
# Example 1:
# Input: nums = [100, 4, 200, 1, 3, 2]
# Output: 4 (The longest consecutive sequence is [1, 2, 3, 4])
# Example 2:
# Input: nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
# Output: 9 (The sequence is [0, 1, 2, 3, 4, 5, 6, 7, 8])

# nums = [100,4,200,1,3,2]
nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]

def rec_func(numset, n,k):
    numset = numset
    n=n
    if n+k in numset:
        k=k+1
        return rec_func(numset, n,k)
    else:
         return k

def longest_sequence(nums):
    numset = set(nums)
    counter = 0
    for n in nums:
        if n-1 not in numset:
            value = rec_func(numset, n, 1)
            if counter<value:
                counter = value

    print(counter)

longest_sequence(nums)


"""optimized version - to avoid recursion depth error"""
def longest_consecutive(nums):
    num_set = set(nums)
    longest = 0

    for n in nums:
        # Check if 'n' is the start of a sequence
        if n - 1 not in num_set:
            current_num = n
            current_streak = 1

            # Keep checking for the next numbers in the sequence
            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1

            # Keep track of the longest sequence found so far
            longest = max(longest, current_streak)

    return longest