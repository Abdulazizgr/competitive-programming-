x = int(input())
for i in range(x):
    y = input()
    if len(y) > 10:
        z = y[0]
        a = len(y) - 2
        b = y[-1]
        print(z + str(a) + b)
    else:
        print(y)
