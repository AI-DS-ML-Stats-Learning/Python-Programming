# Problem 4: Group Anagrams
# LeetCode Link: #49 - Group Anagrams
# Recommended Filename: 004_group_anagrams.py
# Category: Arrays & Hashing
# Difficulty: Medium
# Problem Description
# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# Example
# Input: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
# Output: [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]

# The Clue to Solve it:
# An anagram means that if we sort the words, they will look identical (e.g. "eat", "tea", and "ate" all sort to "aet").

# We can use a Dictionary where:

# The Key is the sorted version of the word: "aet"
# The Value is a list of all matching words: ["eat", "tea", "ate"]
# Hint: You can use defaultdict(list) which we learned in our Collections module to make this very clean!

# Have a think about it, write the code, and let's get that daily streak going!
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

sorted_str = [''.join(sorted(i)) for i in strs]
strs_dict = {x:value for x, value in zip(strs,sorted_str)}

from collections import defaultdict

group = defaultdict(list)

for key in strs_dict:
    group[strs_dict.get(key)].append(key)

print(list(group.values()))