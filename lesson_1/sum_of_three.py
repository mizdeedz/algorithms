# Our code generates a random three-digit number and has to sum up all its digits
# For example, if a number is 349, the code has to print the number 16, because 3 + 4 + 9 = 16


# Solution #1
# O(n)

# from random import randint
# random_number = randint(100, 999)
# print(f'The random number is: {random_number}')
#
# result = 0
# while random_number != 0:
#     result = result + (random_number % 10)
#     random_number = random_number // 10
#
# print(f'The result is: {result}')


# iterations illustration for Solution #1

# 1st iter
# random_number = 647
# result = 0
# while random_number != 0:
#     result = result + (random_number % 10)  # 1st iter: result = 7 (0 + 7) we get 7 because (647 % 10 = 64.7)
#     random_number = random_number // 10  # 1st iter: rand_num = 64 (647 // 10 = 64)

# 2nd iter
# random_number = 64
# result = 7
# while random_number != 0:
#     result = result + (random_number % 10)  # 2nd iter: result = 11 (7 + 4) we get 4 because (64 % 10 = 6.4)
#     random_number = random_number // 10  # 2nd iter: rand_num = 6 (64 // 10 = 6)

# 3rd iter
# random_number = 6
# result = 11
# while random_number != 0:
#     result = result + (random_number % 10)  # 3rd iter: result = 17 (11 + 6) we get 6 because (6 % 10 = 6)
#     random_number = random_number // 10  # 3rd iter: rand_num = 0 (6 // 10 = 0)

# 4th iter
# random_number = 0
# result = 17
# while random_number != 0:  # evaluated as false, loop breaks, and result is printed
#     result = result + (random_number % 10)
#     random_number = random_number // 10


# Solution #2
# O(n)

from random import randint
random_number = randint(100, 999)
print(f'The random number is: {random_number}')

result = 0
for digit in str(random_number):
    result = result + int(digit)

print(f'The result is: {result}')
