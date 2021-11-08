# Given a string, return a reversed string.
# For example, abcde -> edcba


# Solution #1
# O(n)  n = len(s)

# def reverse_str(s):
#     return s[::-1]
#
# s = "12345"
# print(s)
# print(reverse_str(s))


# Solution #2
# O(n)

def reverse_str(s):
    reversed_string = ""

    index = len(s) - 1
    while index >= 0:
        reversed_string = reversed_string + s[index]
        index -= 1

    return reversed_string


s = "12345"
print(s)
print(reverse_str(s))