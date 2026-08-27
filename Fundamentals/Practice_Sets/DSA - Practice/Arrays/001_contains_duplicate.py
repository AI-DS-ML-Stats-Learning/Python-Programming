# Problem Description
# Given an integer array nums, return True if any value appears at least twice in the array, 
# and return False if every element is distinct.

# Examples
# Example 1:
# Input: nums = [1, 2, 3, 1]
# Output: True
# Example 2:
# Input: nums = [1, 2, 3, 4]
# Output: False


''' Approach 1 - My Approach
Time complexity - 
    for sorting the list - O(NlogN) [it used Timsort at the backend]
    for loop - O(N)
    since, O(NlogN) is slower, we consider that to be the Time-C here

Space Complexity - O(N) -> since, we are creating a new variable all together after sorting
'''
# def find_duplicates(data):
#     sorted_Data = sorted(data)

#     j = 0

#     for i in range(len(sorted_Data)-1):
#         if sorted_Data[i] == sorted_Data[i+1]:
#             j += 1
        
#     if j > 0:
#         return True
#     else:
#         return False

''' Approach 2 -> using hash sets

Time complexity - 
    one for loop - O(N)

Space Complexity - O(N) -> since, we are creating a new variable all together and at worst the entire set can be unique
'''
# def find_duplicates(data):

#     new_Set = set()

#     for value in data:
#         if value in new_Set:
#             return True
#         new_Set.add(value)

''' Approach 3 -> using sets/ pythonic way

Time complexity - O(N) because no matter what this will convert the entire set of data into a set 
    (even if 1 Million records and even if there are a chances of finding the duplicate at the start and truncating the program)

Space Complexity - O(N) -> since, we are creating a new variable all together and at worst the entire set can be unique
'''
def find_duplicates(data):
    if len(data) == len(set(data)):
        return False
    else:
        return True

nums = [4, 2, 3, 4]

print(find_duplicates(nums))


