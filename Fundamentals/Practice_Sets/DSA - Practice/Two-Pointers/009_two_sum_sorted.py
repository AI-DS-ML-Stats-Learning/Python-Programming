# Problem Description
# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, 
# find two numbers such that they add up to a specific target number.

# Return the indices of the two numbers, [index1, index2], added by one (1-indexed).

# Constraints:

# Must use only O(1) extra space. (This means you cannot use a Hash Map dictionary like we did in Problem 3!).
# Example
# Input: numbers = [2, 7, 11, 15], target = 9
# Output: [1, 2] (because 2 + 7 = 9. Since it is 1-indexed, indices are 1 and 2)

import time
import tracemalloc

numbers = [2, 7, 11, 15]
target = 9

'''Brute force
Time - O(N2) -> since every combination is explored
'''
tracemalloc.start()
start1 = time.perf_counter()
def two_sum(numbers: int) -> list:
    left = 0
    right = len(numbers) -1

    while left < right:
        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left+1, right+1]
                break
            else:
                right -= 1

        left += 1
        right = len(numbers) -1
    return []

print(two_sum(numbers))

end1 = time.perf_counter()

current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()
print(f"Time taken: {end1 - start1:.8f} seconds")
print(f"Peak RAM used: {peak / 1024 / 1024:.2f} MB")

'''Optimized way
Time - O(N)'''

tracemalloc.start()
start2 = time.perf_counter()
def two_sum_optimized(numbers: int) -> list:
    left = 0
    right = len(numbers) - 1

    while left < right:
        curr_sum = numbers[left] + numbers[right]

        if curr_sum == target:
            return [left+1, right+1]
        elif curr_sum > target:
            right -=1
        else:
            left += 1

    return []

print(two_sum_optimized(numbers))

end2 = time.perf_counter()

current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()

print(f"Time taken: {end2 - start2:.8f} seconds")
print(f"Peak RAM used: {peak / 1024 / 1024:.2f} MB")