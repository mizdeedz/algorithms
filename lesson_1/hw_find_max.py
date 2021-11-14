# Find max number from 3 values, entered manually from a keyboard.
# Example: 124, 21, 32. Result = 124.

# My Solution
# Time Complexity: O(1)

num_1 = int(input('Enter the first number: '))
num_2 = int(input('Enter the second number: '))
num_3 = int(input('Enter the third number: '))

result = max(num_1, num_2, num_3)

print(f'The max number is {result}')


# Alternate (Instructor) Solution #1
# O()

# def find_max(a, b, c):
#     return max(a, b, c)
#
#
# number_1 = int(input('Provide your 1-number: '))
# number_2 = int(input('Provide your 2-number: '))
# number_3 = int(input('Provide your 3-number: '))
#
# print(find_max(number_1, number_2, number_3))


# Alternate (Instructor) Solution #2
# O(1)

# def find_max(a, b, c):
#     if a > b and a > c:
#         return a
#     if b > a and b > c:
#         return b
#     return c
