# When given a list of elements, find the two lowest elements.
# They can be equal to each other or different.
# Example: [198, 3, 4, 9, 10, 9, 2], Return: 2, 3

# My Solution
# Time Complexity: O(1)

def two_lowest(arr):
    first_lowest = min(arr)
    arr.remove(first_lowest)
    second_lowest = min(arr)

    return first_lowest, second_lowest


test_list = [198, 3, 4, 9, 10, 9, 2]
print(two_lowest(test_list))


# Alternate (Instructor) Solution #1
# O(log n)

# def find_lowest(arr):
#     arr.sort()
#     return arr[:2]
#
#
# list_to_test() = []
# print(list_to_test)
# print(below_mean(list_to_test))