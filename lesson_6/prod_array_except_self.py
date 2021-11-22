# Given an integer array nums, return an array answer such that
# answer[i] is equal to the product of all the elements of nums, except nums[i].
# You must write an algorithm that runs in O(n) time
# and without using the division operation.

# Example:
# Input: nums = [1, 2, 3, 4]
# Output: [24, 12, 8, 6]  # (2*3*4, 1*3*4, 1*2*4, 1*2*3)


# Solution #1
# O(n^2)

# def mult_of_array(arr):
#     result = [1] * len(arr)  # now we have the same number of elements as in our arr, but they are all set to 1
#
#     for i in range(0, len(arr)):
#         for j in range(0, len(arr)):
#             if i != j:
#                 result[i] = result[i] * arr[j]
#
#     return result
#
#
# test_arr = [1, 2, 3, 4]
# print(test_arr)
# print(mult_of_array(test_arr))


# Solution #2
# O(n)

def mult_of_array(arr):
    result = [1] * len(arr)

    for i in range(0, len(arr) - 1):
        result[i + 1] = result[i] * arr[i]

    for i in range(0, len(arr) - 1):
        result[-1 - i] = result[-1 - i] * result[0]
        result[0] = result[0] * arr[-1 - i]

    return result


test_arr = [1, 2, 3, 4]
print(test_arr)
print(mult_of_array(test_arr))
