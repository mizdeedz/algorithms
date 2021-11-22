# Given an integer array nums, return True if any value appears at least twice in the array
# and return False if every element is distinct.
# Examples:
# Input: [1, 2, 3, 1], Output: True
# Input: [1, 2, 3, 4], Output: False


# Solution #1
# O(1)

def is_duplicate(arr):
    if len(arr) > 1:
        nums_set = set(arr)
        if len(arr) > len(nums_set):
            return True

    return False


test_arr_pos = [1, 2, 3, 4, 5, 2]
test_arr_neg = [1, 2, 3, 4, 5, 6]
print(is_duplicate(test_arr_pos))
print(is_duplicate(test_arr_neg))


# Solution #2 (example only - unfinished code)
# O()

# def is_duplicate(arr):
#     set_nums = set()
#     for i in arr:
#         if i in set_nums:
#             return True
#
#     return False
#
#
# test_arr_pos = [1, 2, 3, 4, 5, 2]
# test_arr_neg = [1, 2, 3, 4, 5, 6]
# print(is_duplicate(test_arr_pos))
# print(is_duplicate(test_arr_neg))
