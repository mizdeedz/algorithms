# Given a string in the form "AAAABBBBCCCCCDDEEEE" compress it to become "A4B4C5D2E4"
# For this problem, you can falsely "compress" strings of single or double letters
# For instance, it is okay for "AAB" to return "A2B1" even though this technically takes more space.
# The function should also be case sensitive, so that a string "AAAaaa" returns "A3a3"


# Solution #1
# O(n)

def compress(s):
    result = ""
    length = len(s)

    # edge cases
    if length == 0:
        return ""
    if length == 1:
        return s + "1"

    cnt = 1
    i = 1

    while i < length:
        if s[i] == s[i - 1]:
            cnt += 1
        else:
            result = result + s[i - 1] + str(cnt)
            cnt = 1

        i += 1

    result = result + s[i - 1] + str(cnt)

    return result


s = "AAAABBBBCCCCCDDEEEE"
s2 = "AABBCCabc"  # outcome should be: A2B2E2a1b1c1
print(compress(s))
print(compress(s2))
