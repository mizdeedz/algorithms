# Example of Merge Sort, reference recursion
# O(n log n)


# O(log n)
def merge_sort(arr):
	if len(arr) <= 1:
		return arr
	middle = len(arr) // 2

	return merge_arrays(merge_sort(arr[:middle]), merge_sort(arr[middle:]))


# O(n)
def merge_arrays(left_array, right_array):
	merged_array = []
	i = j = 0
	while i < len(left_array) or j < len(right_array):
		if i == len(left_array):
			merged_array.append(right_array[j])
			j += 1
			continue
		if j == len(right_array):
			merged_array.append(left_array[i])
			i += 1
			continue
		# this was all edge case
		# now is regular
		if left_array[i] <= right_array[j]:
			merged_array.append(left_array[i])
			i += 1
		else:
			merged_array.append(right_array[j])
			j += 1

	return merged_array


test_list = [2, 7, 6, 1, 10, 5, 4, 8]
print(test_list)
print(merge_sort(test_list))
