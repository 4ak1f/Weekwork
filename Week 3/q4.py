s = input("Enter a string: ")
count = 0

for ch in s:
    if ch in "aeiouAEIOU":
        count += 1
if count > 0:
    print(count)
else:
    print("No vowels in the string")