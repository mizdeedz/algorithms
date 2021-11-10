# Given an array of integers nums and an integer target.
# Return two numbers from each array such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.
# Input: [3, 7, 4, 9, 15, 3], 6
# Output: 3, 3 (3 + 3 = 6)


# Solution #1
# O(n)?

def pair_sum(arr, k):  # arr = [] target number = 6
    if len(arr) < 2:
        return -1

    sum_set = set()

    for num in arr:
        target = k - num  # given (6) - current element (3) = 3 (target value to find in list)

        if target not in sum_set:
            sum_set.add(num)
        else:
            return [target, num]


test_arr = [3, 7, 4, 9, 15, 3]
test_target = 6  # 3, 3
test_target2 = 18  # 15 and 3
print(pair_sum(test_arr, test_target))
print(pair_sum(test_arr, test_target2))