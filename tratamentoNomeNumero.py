"""
The objective of this code is to handle special cases when the user is expected to input
a string but, for some reason, includes a number in it or within the string.

Example 1: Write your full name: Henrique Flavio Guimaraes3
Example 2: Write your full name: 3Henrique Flavio Guimaraes
Example 3: Write your full name: henrique25 flavio Guimaraes
"""

name = input("\nPlease, write your full name>>> ").title().strip()

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

for i in numbers:
    while name.count(i) >= 1:
        print("\nYour name cannot contain numbers!\n")
        name = input("Please, write your full name again: ").title().strip()

print(f"\nHello {name}! Welcome!!!")
