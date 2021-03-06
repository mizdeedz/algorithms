# Write a function to check whether two given strings are an anagram of each other or not
# An anagram of a string, is another string that contains the same characters, only order of characters can be different
# For example, "abcd" and "dabc" are an anagram of each other


# Solution #1
# O()

# def is_anagram(s1, s2):
#     if len(s1) != len(s2):
#         return False
#
#     return sorted(s1) == sorted(s2)
#
# print(is_anagram("aabbccdd", "bbaaddcc"))
# print(is_anagram("aabbccdd", "bbaaddccxyz"))


# Solution #2
# O()

def is_anagram(s1, s2):
    if len(s1) != len(s2):
        return False

    count = {}

    for letter in s1:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1

    for letter in s2:
        if letter in count:
            count[letter] -= 1
        else:
            count[letter] = 1

    for index in count:
        if count[index] != 0:
            return False

    return True

print(is_anagram("aabbccdd", "bbaaddcc"))
print(is_anagram("aabbccdd", "bbaaddccxyz"))