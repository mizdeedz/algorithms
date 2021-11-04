# Find max number from 3 values, entered manually from a keyboard.
# Example: 124, 21, 32. Result = 124.

# My Solution
# Time Complexity: O(1)

num_1 = int(input('Enter the first number: '))
num_2 = int(input('Enter the second number: '))
num_3 = int(input('Enter the third number: '))

result = max(num_1, num_2, num_3)

print(f'The max number is {result}')