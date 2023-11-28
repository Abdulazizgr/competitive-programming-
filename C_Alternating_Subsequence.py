def max_sub(arr: list, n):
    count = 0
    sub_array = []

    for i in range(n):
        if i == 0 or arr[i]/arr[i-1] > 0:
            sub_array.append(arr[i])
        else:
            count += max(sub_array)
            sub_array = [arr[i]]

    count += max(sub_array)
    return count


a = int(input())
for _ in range(a):
    n = int(input())
    arr = [int(i) for i in input().split()]
    print(max_sub(arr, n))
