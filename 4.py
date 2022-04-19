import re

s = input("Enter the string: ")
c = input("Enter the character to double: ")

print(f"New string: {re.sub(c, c+c, s)}")
