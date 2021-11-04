# User inputs two numbers. One number is assigned to a variable, the other number is assigned to another variable.
# The task is to invert the variables, so that the first variable contains the second number,
# while the first number is in the second variable.


# Solution #1
# O(1)

# a = 5
# b = 10
#
# x = a
# a = b
# b = x


# Solution #2
# O(1)

# a = int(input('Input value a: '))
# b = int(input('Input value b: '))
#
# print(f'a = {a}, b = {b}')
#
# temp = a
# a = b
# b = temp
#
# print(f'a = {a}, b = {b}')


# Solution #3
# O(1)

# a = int(input('Input value a: '))
# b = int(input('Input value b: '))
#
# print(f'a = {a}, b = {b}')
#
# a, b = b, a
#
# print(f'a = {a}, b = {b}')


# Solution #4
# O(1)

a = int(input('Input value a: '))
b = int(input('Input value b: '))

print(f'a = {a}, b = {b}')  # a = 10, b = 5

a = a + b  # 10 + 15 = 15; a = 15, b = 5
b = a - b  # 15 - 5 = 10; a = 15, b = 10
a = a - b  # 15 - 10 = 5; a = 5, b = 10

print(f'a = {a}, b = {b}')  # a = 10, b = 5

