# Given an array of strings strs, group the anagrams together.
# You can return the answer in any order.

# An anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
# typically using all the original letters exactly once.

# Example:
# Input: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
# Output: [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]


# Solution #1
# O(n)

def group_anagrams(strs):
    hash_map = {}
    for word in strs:
        key = "".join(sorted(word))

        if key in hash_map.keys():
            hash_map[key].append(word)
        else:
            hash_map[key] = []
            hash_map[key].append(word)

    return list(hash_map.values())


test_strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(test_strs)
print(group_anagrams(test_strs))
