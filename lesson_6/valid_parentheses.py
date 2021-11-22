# Given a string s containing just the characters '(', ')', '{', '}', '[', ']'
# determine if the input string is valid.
# An input string is valid if:
# Open brackets must be closed by the same type of brackets
# Open brackets must be closed in the correct order

# Examples:
# Input: "()[]{}", Output: True
# Input: "([)]", Output: False


# Solution #1
# O(n)

def is_valid_parentheses(s):
    parentheses = {'(': ')', '[': ']', '{': '}'}
    control = []

    for i in s:
        if i in parentheses:
            control.append(parentheses[i])
        elif len(control) == 0:
            return False
        elif control.pop() != i:
            return False

    if len(control) == 0:
        return True

    return False


test_s_pos = "()[]{}"
test_s_neg = "([)]"
print(is_valid_parentheses(test_s_pos))
print(is_valid_parentheses(test_s_neg))
