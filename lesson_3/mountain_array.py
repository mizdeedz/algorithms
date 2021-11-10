# Given an array of integers, return true if the following conditions are fulfilled:
#   length of array is bigger than or equal to 3
#   there exists some index i such that:
#     a[] <a[] < ... <a[i]
#     a[] > a[i+1] > ... > a[a.size-1]
#
# Basically, find if there is an increasing subarray, followed by a decreasing subarray.
# [3, 5, 5] -> false
# [3, 4, 5, 2] -> true


# Solution #1
# O(n)

def is_mountain(arr):
    i = 1

    while i < len(arr) and arr[i] > arr [i - 1]:
        i = i + 1

    if i == 1 or i == len(arr):
        return False

    while i < len(arr) and arr[i] < arr [i - 1]:
        i = i + 1

    return i == len(arr)


test_arr_neg = [3, 5, 5]  # -> False
test_arr_pos = [3, 4, 5, 2]  # -> True
print(is_mountain(test_arr_neg))
print(is_mountain(test_arr_pos))