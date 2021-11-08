# Built-In String Methods


# Escaping Characters

# txt = "She said \"Never let go\"."
# print(txt)


# The 'in' Syntax

# txt = "This is my string"
# print("string" in txt)
# print("int" in txt)


# Indexing & Slicing Strings

# txt = "This is my string"
# print(txt[0])
# print(txt[1])
# print(txt[-1])
# print(txt[:4])
# print(txt[1:4])
# print(txt[-5:])


# String Concatenation

# a = "One fish "
# b = "Two fish"
# print(a + b)


# Iterate String (for loop)

# txt = "string"
# for char in txt:
#     print(char)


# String Method .len()

# txt = "string"
# print(len(txt))


# String Method .lower()

# txt = "This Is My String"
# print(txt)
# print(txt.lower())


# String Method .upper()

# txt = "This Is My String"
# print(txt)
# print(txt.upper())


# String Method .split()
#
# txt = "This is my string"
# print(txt)
# print(txt.split())
# print(txt.split('is'))
# print(txt.split('Is'))


# String Method .join()

# txt = '-'.join(['one', 'two', 'three'])
# txt2 = ' apple '.join(['one', 'two', 'three'])
# print(txt)
# print(txt2)


# String Method .strip()

# txt = "    this is our string    "
# txt_2 = ".    this is our string    "
# print(txt)
# print(txt.strip())
# print(txt_2)
# print(txt_2.strip("."))  # removes the "."
# print(txt_2.strip(".").strip())  # removes the "." and removes the whitespace


# String Method .replace()

# txt = "This is our string"
# print(txt)
# print(txt.replace("This", "That"))
# print(txt.replace("s", "S"))


# String Method .find()

# txt = "This is our string"
# print(txt)
# print(txt.find("T"))
# print(txt.find("t"))
# print(txt.find("z"))


# String Method .format()

# txt = "This is our {}th lesson"
# txt_2 = "This is our {}th lesson out of {}"
# print(txt)
# print(txt.format("4"))
# print(txt_2)
# print(txt_2.format("4", "9"))