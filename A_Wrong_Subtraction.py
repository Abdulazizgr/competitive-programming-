n, a = map(int, input().split())

for i in range(1, a+1):
    r = n % 10
    if r == 0:
        n /= 10
    else:
        n -= 1

print(int(n))
