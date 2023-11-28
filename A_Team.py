x = int(input())
count = 0
for i in range(x):
    an = [int(i) for i in input().split()]
    a = an.count(1)
    if a > 1:
        count += 1
print(count)
