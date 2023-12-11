import sys
max_ = -sys.maxsize
min_ = sys.maxsize
n, m = map(int, input().split())
arr = list(map(int, input().split()))

if n == m:
    print(max(arr))
else:
    divider = n // m
    for i in range(0, n, divider):
        cnt = 0
        for j in range(i, i + divider):
            cnt += arr[j]
        max_ = max(max_, cnt)
        min_ = min(min_, max_)

    print(min_)