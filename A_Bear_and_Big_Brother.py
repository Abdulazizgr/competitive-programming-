a, b = map(int, input().split())

c = 0
if a > b:
    c = 0
else:
    while a <= b:
        a *= 3
        b *= 2
        c += 1

print(c)
