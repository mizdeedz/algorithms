# When given a list, the program should return a list of all the elements below the original list’s arithmetical mean.
# The arithmetical mean is the sum of all elements divided by the number of elements.
# Example: [1, 3, 5, 6, 4, 10, 2, 3] (The arithmetical mean is 4.25), Return [1, 3, 4, 2, 3]

# My Solution
# Time Complexity: O(n)

def below_mean(arr):
    mean = sum(arr) // len(arr)
    new_list = []

    for i in range(len(arr)):
        if arr[i] <= mean:
            new_list.append(arr[i])

    return new_list


test_list = [1, 3, 5, 6, 4, 10, 2, 3]
print(below_mean(test_list))