s = input("Enter the string: ")
s0 = input("Enter the substring: ")

count = 0
for i in range(len(s)-len(s0)+1):
    if s[i:i+len(s0)] == s0:
        count += 1

print(f"The substring occurs in the string {count} times")
