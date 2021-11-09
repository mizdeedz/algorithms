# Given a string, determine if it consists of all unique characters.
# For example, the string 'abcde' has all unique characters and should return True.
# The string 'aabcde' contains duplicate characters and should return False.

# My Solution
# Time Complexity: O(1)

def uni_char(s):
	return len(set(s)) == len(s)


pos_test = "abcde"
neg_test = "abcdde"

print(uni_char(pos_test))
print(uni_char(neg_test))