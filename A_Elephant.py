n = int(input())
a = [5, 4, 3, 2, 1]
ans = 0

for i in range(5):
    ans += n // a[i]
    n = n % a[i]

print(ans)
