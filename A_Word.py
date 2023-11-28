s = input()
count_up = 0
count_low = 0

for char in s:
    if char.isupper():
        count_up += 1
    else:
        count_low += 1

if count_up > count_low:
    result = s.upper()
else:
    result = s.lower()

print(result)
