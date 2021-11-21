# Implement the insertion sort algorithm that is sorting in descending order.

# My Solution
# O(n^2)

def desc_insertion_sort(arr):

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key > arr[j]:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = key

    return arr


test_list = [2, 7, 6, 1, 10, 5, 4, 8]
print(test_list)
print(desc_insertion_sort(test_list))
