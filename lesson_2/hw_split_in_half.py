# Given a string. Split it into two equal parts.
# Swap these parts and return the result.
# If the string has odd characters, the first part should be one character greater than the second part.
# Example: string = 'bbbbbcaaaaa'. Result = ‘aaaaabbbbbc’.

# My Solution
# Time Complexity: O(1)

def split_in_half(s):
    length = len(s)
    half = length // 2
    add = 0

    if length % 2:
        add = 1

    left = s[:half + add]
    right = s[half + add:]

    return right + left


test_str = 'bbbbbcaaaaa'
print(split_in_half(test_str))


# Alternate (Instructor) Solution #1
# O(1)

# def split_in_half(s):
#     length = len(s)
#     half = length // 2   # leaves us with 1 int
#     add = 0  # if string is odd, add this
#
#     # if % results in 0 it is even
#     # if % results in remainder it is odd
#
# 	if length % 2:
#         add = 1
#
#     # set left side to half plus 1 if odd
#     # or half plus 0 if equal parts
#
# 	left = s[:half + add]
#
#     # set right side from half + add
#     # until the end of string
#
# 	right = s[half + add:]
#
#     print(left)  # bbbbbc
#     print(right)  # aaaaa
#
#     # concatenating 2 strings, in reverse order
#
# 	return right + left
#
#
# test_str = 'bbbbbcaaaaa'
# print(split_in_half(test_str))