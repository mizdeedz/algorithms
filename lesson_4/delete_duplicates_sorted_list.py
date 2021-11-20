# Write a program that takes as input a sorted array and updates it so that all duplicates have been removed,
# and the remaining elements have been shifted left to fill the emptied indices.
# Fill the remaining indices with zeros.
# Return the number of valid elements.
# You cannot use sets for this coding challenge.

# Example:
# [1, 2, 4, 4, 5, 6, 7, 10, 10, 18, 21, 21, 22]  # len = 13
# [1, 2, 4, 5, 6, 7, 10, 18, 21, 22, 0, 0, 0]  # len = 13


# Solution #1
# O(n)

def delete_duplicates(arr):
    right_index = 1

    if len(arr) == 1:
        return 1

    for i in range(1, len(arr)):
        if arr[right_index - 1] != arr[i]:
            arr[right_index] = arr[i]
            right_index = right_index + 1

    for i in range(right_index, len(arr)):
        arr[i] = 0

    print(arr)
    return right_index


test_list = [1, 2, 4, 4, 5, 6, 7, 10, 10, 18, 21, 21, 22]
print(test_list)
print(delete_duplicates(test_list))
