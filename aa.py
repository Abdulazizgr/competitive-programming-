from collections import Counter
n = True
x = int(input())
while (n):
    x += 1
    x = str(x)
    co = Counter(x)
    an = [i for i in co.values() if i < 2]
    if len(an) != len(x):
        x = int(x)
    else:
        x = int(x)
        print(x)
        n = False
