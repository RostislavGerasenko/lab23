s = input("Enter the string: ")
print(f"There are {sum(ord('A') <= ord(c) <= ord('Z') for c in s)} uppercase Latin characters")
