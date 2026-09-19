# Problem Description
# A phrase is a palindrome if, after converting all uppercase letters into 
# lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward.
# Alphanumeric characters include letters and numbers.

# Given a string s, return True if it is a palindrome, or False otherwise.

# Examples
# Example 1:
# Input: s = "A man, a plan, a canal: Panama"
# Output: True (Cleaned: "amanaplanacanalpanama", which reads the same backwards)
# Example 2:
# Input: s = "race a car"
# Output: False (Cleaned: "raceacar", which backwards is "racaecar" - not a match)

s = "A man, a plan, a canal: Panama"

'''without 2 pointers
space - O(N)
time - O(N)
'''
k = []
for i in s.lower():
    if i.isalnum():
        k.append(i)
    else:
        pass

print(''.join(k))
print(''.join(k[::-1]))
if ''.join(k) == ''.join(k[::-1]):
    print("palindrome")
else:
    print("not a palindrome")


'''2-pointer approach'''
def check_palindrome(s: str) -> bool:

    left = 0
    right = len(s) -1

    while left < right:
        while left < right and not s[left].isalnum():
            left +=1

        while left < right and not s[right].isalnum():
            right -= 1

        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True

print(check_palindrome(s))
