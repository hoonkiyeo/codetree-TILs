import sys
n, m = map(int, input().split())
arr = list(map(int, input().split()))

for i in range(max(arr), sum(arr)+1):
    tmp = []
    val_sum = arr[0]
    for j in range(1, n):
        if val_sum + arr[j] > i:
            tmp.append(val_sum)
            val_sum = arr[j]
        else:
            val_sum += arr[j]
    tmp.append(val_sum)
    if len(tmp) <= m:
        print(i)
        break