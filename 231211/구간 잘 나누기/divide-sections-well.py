n, m = map(int, input().split())
arr = list(map(int, input().split()))

ans = sum(arr)
for i in range(max(arr), sum(arr)+1):

    section = 1
    cnt = 0

    for j in range(n):
        if cnt + arr[j] > i:
            cnt = 0
            section += 1
        cnt += arr[j]

    if section <= m:
        ans = min(ans, i)
print(ans)