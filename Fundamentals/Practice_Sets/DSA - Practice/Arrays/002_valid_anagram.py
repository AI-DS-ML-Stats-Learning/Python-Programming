# Problem Description
# Given two strings s and t, return True if t is an anagram of s, and False otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
# typically using all the original letters exactly once. (e.g. "silent" and "listen" are anagrams).

# Examples
# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: True
# Example 2:
# Input: s = "rat", t = "car"
# Output: False

s = "anagram"
t = "nagaram"

# '''The Sorting approach (O(NlogN))'''

# if sorted(s) == sorted(t):
#     print(True)
# else:
#     print(False)

'''
time complexity - O(N) + O(N) = O(N)
space compplexity - O(N) + O(N) = O(N)
'''

# '''The Hash Map / Dictionary approach (O(N))'''

# def is_anagram_raw_dict(s: str, t: str) -> bool:
#     # If the lengths are different, they cannot be anagrams
#     if len(s) != len(t):
#         return False
        
#     count_s = {}
#     count_t = {}
    
#     # Loop through both strings simultaneously
#     for i in range(len(s)):
#         # .get(char, 0) returns 0 if the character is not in the dictionary yet
#         count_s[s[i]] = count_s.get(s[i], 0) + 1
#         count_t[t[i]] = count_t.get(t[i], 0) + 1
        
#     # Compare the two dictionaries
#     return count_s == count_t

# '''The Counter one-liner approach.'''
from collections import Counter

if Counter(t) == Counter(s):
    print(True)
else:
    print(False)
