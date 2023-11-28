s = input()
arr = []
for char in s:
    if char != '+':
        arr.append(int(char))
arr.sort()
result = '+'.join(str(num) for num in arr)
print(result)
