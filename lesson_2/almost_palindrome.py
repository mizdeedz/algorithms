# Given a non-empty string s, you may delete at most one character.
# Judge whether you can make it a palindrome.
# The string will only contain lowercase characters a-z and it's not a palindrome
# For example, "radkar" is almost a palindrome. "radario" is not almost a palindrome.


# Solution #1
# O(n)  n = len(s)

def is_almost_palindrome(s):
    for i in range(len(s)):
        t = s[:i] + s[i + 1:]
        if t == t[::-1]:
            return True

    return s == s[::-1]  # or return False

str_pos = "radkar"
str_neg = "radarop"
print(is_almost_palindrome(str_pos))  # True
print(is_almost_palindrome(str_neg))  # False