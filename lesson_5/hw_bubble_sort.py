# Implement the bubble sort algorithm that is sorting in descending order.

# My Solution
# O(n^2)

def desc_bubble_sort(arr):

    for i in range(len(arr)):
        for j in range(len(arr) - 1 - i):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


test_list = [2, 7, 6, 1, 10, 5, 4, 8]
print(test_list)
print(desc_bubble_sort(test_list))
