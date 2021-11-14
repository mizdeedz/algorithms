# Count odd and even numbers. Count odd and even digits of the whole number.
# Example: entered number is 34560, then 3 digits will be even (4, 6, and 0) and 2 odd digits (3 and 5).

# My Solution
# Time Complexity: O(n)

num = int(input('Enter a whole number: '))
odd_count = 0
even_count = 0

for n in str(num):
    if int(n) % 2 != 0:
        odd_count += 1
    else:
        even_count += 1


print(f'There are {odd_count} odd numbers and {even_count} even numbers')


# Alternate (Instructor) Solution #1
# O()

# def count_odd_even(number):
#     odds = 0
#     evens = 0
#
#     while number != 0:
#         current_digit = number % 10
#         if current_digit % 2:
#             odds += 1
#         else:
#             evens += 1
#         number = number // 10
#
#     return ['Evens: ' + str(evens), 'Odds: ' + str(odds)]
#
#
# number = int(input('Enter your number: '))
# print(count_odd_even(number))
