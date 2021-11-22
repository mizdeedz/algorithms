# Example of Linear Search
# O(n)


def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i

    return None


test_arr = [1, 4, 6, 8, 3, 2, 10, 7]
print(linear_search(test_arr, 10))
print(linear_search(test_arr, 99))  # edge case, which should return None
