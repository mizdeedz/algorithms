# Example of Binary Search
# O(log n)


def binary_search(arr, x):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]
        if guess == x:
            return mid
        if guess > x:
            high = mid - 1
        else:
            low = mid + 1

    return None


test_arr = [1, 3, 5, 8, 10, 15, 19]
print(binary_search(test_arr, 5))
print(binary_search(test_arr, 7)) # edge case, which should return None
