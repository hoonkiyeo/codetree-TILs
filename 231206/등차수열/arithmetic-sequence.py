n = int(input())
arr = list(map(int, input().split()))

max_cnt = 0
for i in range(1, 101):
    cnt = 0
    for j in range(n):
        for k in range(j+1, n):
            if (arr[j] + arr[k]) / 2 == i:
                cnt += 1
    max_cnt = max(max_cnt, cnt)
print(max_cnt)