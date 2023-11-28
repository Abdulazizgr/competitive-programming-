s = input()
s = ''.join(sorted(s))
l = len(s)
ans = 0
for i in range(1, l):
    if s[i] != s[i-1]:
        ans += 1

if ans % 2 == 1:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
