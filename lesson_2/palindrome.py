# Given a string, write a python function to check if it is palindrome or not
# A string is said to be a palindrome if the reverse of the string is the same as string
# For example, "radar" is a palindrome, but "radix" is not a palindrome


# Solution #1
# O(1)

def is_palindrome(s):
	return s == s[::-1]

str_pos = "radar"
str_neg = "radix"
print(is_palindrome(str_pos))  # True
print(is_palindrome(str_neg))  # False