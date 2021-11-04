# When user enters a number, its factorial is displayed


# Solution #1
# O(n)

# import math
#
# number = int(input('Input your number: '))
# factorial = math.factorial(number)
#
# print(f'The factorial of {number} is {factorial}')


# Solution #2
# O(n)

number = int(input('Input your number: '))

factorial = 1
if number != 0:
    for n in range(1, number + 1):
        factorial = factorial * n  # factorial *= n

print(f'The factorial of {number} is {factorial}')

# number = 5
# factorial = 1
# 1st iter, factorial = 1
# 2nd iter, factorial = 2 (1 * 2)
# 3rd iter, factorial = 6 (2 * 3)
# 4th iter, factorial = 24 (6 * 4)
# 5th iter, factorial = 120 (24 * 5)