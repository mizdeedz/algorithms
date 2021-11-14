# Compute the sum of digits in all numbers from 1 to n.
# When a user enters a number n, find the sum of digits in all numbers from 1 to n.
# Example: n = 5. Result = 1 + 2 + 3 + 4 + 5 = 15

# My Solution
# Time Complexity: O(n)

num = int(input('Enter a number: '))
result = 0

for n in range(1, num + 1):
    result += n


print(f'The sum is {result}')


# Alternate (Instructor) Solution #1
# O(n)

# def sum_n(n):
#     final_result = 0
#     for x in range(n + 1):
#         final_result = final_result + x
#     return final_result
#
# number = int(input('Provide your number: '))
# print(sum_n(number))


# Alternate (Instructor) Solution #2
# O(1)

# def sum_n(n):
#     return (n * (n + 1)) / 2
