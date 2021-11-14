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