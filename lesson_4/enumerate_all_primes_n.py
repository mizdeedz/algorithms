# Write a program that takes an integer argument and returns all the primes between 1 and that integer.
# For example, if the input is 18, you should return [2, 3, 5, 7, 11, 13, 17]
# A natural number is called a prime if it is bigger than 1 and has no divisors other than 1 and itself.


# Solution #1
# O(n^2)

def gen_prime_nums_to_n(n):
    primes = []

    for i in range(2, n + 1):
        for p in range(2, i + 1):
            if p == i:
                primes.append(i)
                break
            if i % p == 0:
                break

    return primes


max_prime = 18
print(gen_prime_nums_to_n(max_prime))


# Solution #2
# O(n^2)

# def gen_prime_nums_to_n(n):
#     primes = []
#     is_prime = [False, False] + [True] * (n - 1)  # n = 7 [False, False, True, True, True, True, True, True]
#
#     for p in range(2, n + 1):
#         if is_prime[p]:
#             primes.append(p)
#             for i in range(p, n + 1, p):
#                 is_prime[i] = False
#
#     return primes
#
#
# max_prime = 18
# print(gen_prime_nums_to_n(max_prime))
