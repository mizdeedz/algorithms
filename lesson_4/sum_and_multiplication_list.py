# Given an array. Calculate sum and multiplication of all elements.
# Return the list, calculated sum, and multiplication of elements.
# Example: [1, 7, 3], Return: [11, 21]


# Solution #1
# O(n)

def find_sum_and_mult(arr):
    sum_result = 0
    mult_result = 1

    for num in arr:
        sum_result = sum_result + num
        mult_result = mult_result * num

    return [sum_result, mult_result]


test_list = [1, 7, 3]
print(test_list)
print(find_sum_and_mult(test_list))
