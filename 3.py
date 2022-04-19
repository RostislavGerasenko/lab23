s = input("Enter the string: ")
print(f"There are {sum(ord('a') <= ord(c) <= ord('z') for c in s)} lowercase Latin characters")
