# Example of Recursion, to better understand merge sorting
# O()

def recursion(number):
    print(number)
    if number == 0:
        return
    number = number - 1
    recursion(number)


recursion(10)
