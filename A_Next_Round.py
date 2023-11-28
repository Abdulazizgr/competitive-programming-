x, y = input().split()
an = [int(i) for i in input().split()]
count = 0

for i in an:
    if i > int(y):
        count += 1

print(count)
