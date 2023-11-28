

nums = [1, 2, 3, 1, 1, 3]
count = 0
fre = {}

for num in nums:
    if num in fre:
        count += fre[num]

        print(count)
        fre[num] += 1

    else:
        fre[num] = 1

print(count)
