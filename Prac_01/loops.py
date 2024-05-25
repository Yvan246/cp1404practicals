"""
loop that displays all the odd numbers between
1 and 20 with a space between each one.
"""

"""1 and 20 with a space between each one."""
for i in range(1, 21, 2):
    print(i, end=' ')
print()


""" count in 10s from 0 to 100"""
print("A)")
for i in range(0, 110, 10):
    print(i, end=' ')
print()


"""count down from 20 to 1"""
print("B)")
for i in range(20, 0, -1):
    print(i, end=' ')
print()


"""print n stars. Ask the user for a number, then print that many stars (*), all on one line."""
print("C) ")
numbers_of_stars = int(input("Number of stars? "))
for num in range(numbers_of_stars):
    print("*", end=" ")
print()


"""print n lines of increasing stars. Using the same number above, print lines of increasing stars, starting at 1 
with no blank line."""
print("D)")
for num in range(numbers_of_stars):
    for n in range(num + 1):
        print("*", end=" ")
    print()
