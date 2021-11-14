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


# Alternate (Instructor) Solution #1
# O(1)

# def uni_char(s):
# 	return len(set(s)) == len(s)
#
# 	# s = aabcde
# 	# set(s) = {'a', 'b', 'c', 'd', 'e'}
#
# 	# if the length matches then they are unique
# 	# if it doesn't match there are repeated letters
#
#
# pos_test_str = "abcde"
# neg_test_str = "abcdde"
#
# print(uni_char(pos_test_str))  # True
# print(uni_char(neg_test_str))  # False


# Alternate (Instructor) Solution #2
# O(n)

# def uni_char(s):
# 	chars = set()
#
# 	for char in s:
# 		if char in chars:
# 			return False
# 		else:
# 			chars.add(char)
#
# 	return True
#
# 	# because if all characters were added
# 	# we know it is true, otherwise False
#
#
# pos_test_str = "abcde"
# neg_test_str = "abcdde"
#
# print(uni_char(pos_test_str))  # True
# print(uni_char(neg_test_str))  # False