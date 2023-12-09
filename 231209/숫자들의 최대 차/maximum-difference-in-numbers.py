n,k = map(int, input().split())
nums = [int(input()) for _ in range(n)]

max_cnt = 0
for i in range(n):
    a = nums[i]
    cnt = 1
    for j in range(n):
        if i == j:
            continue
        b = nums[j]
        if b >= a and b - a <= k:
            cnt += 1
    max_cnt = max(max_cnt, cnt)
print(max_cnt)