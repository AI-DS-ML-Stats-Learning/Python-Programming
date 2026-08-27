# Problem Description
# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

# Examples
# Example 1:
# Input: nums = [1, 1, 1, 2, 2, 3], k = 2
# Output: [1, 2] (because '1' appears 3 times, '2' appears 2 times, and '3' appears 1 time)
# Example 2:
# Input: nums = [1], k = 1
# Output: [1]

nums = [1, 1, 1, 2, 2, 3,3]
k = 2

'''Pythonic way - using counters/collections

Time Complexity - O(NlogK)
Space Complexity - O(N)
'''
from collections import Counter

# print(Counter(nums).most_common(2)) -  this prints the tuple of values

frequent_list = [value for value, freq in Counter(nums).most_common(2)]

print(frequent_list)

'''
Bucket Sort Approach - Optimal way

# Count the frequencies in a dictionary.
# Create a list of empty lists (buckets) of size len(nums) + 1, where the index represents the frequency count.
# Place each number into the bucket corresponding to its frequency.
# Scan the buckets from the end (highest frequency) to the beginning, collecting elements until you have k items.

Time - 
Space - O(N)
'''
count = {}
for i in nums:
    count[i] = count.get(i, 0) +1

buckets = [[] for _ in range(len(nums)+1)]

for num, frequency in count.items():
    buckets[frequency].append(num)

# for i in range(len(buckets)):
#     print(buckets[i])

final_list = []
c = 0
for i in buckets[::-1]:
    for j in i:
        if c==k:
            break
        elif c<k and j:
            final_list.append(j)
            c +=1
        

print(final_list)
        





