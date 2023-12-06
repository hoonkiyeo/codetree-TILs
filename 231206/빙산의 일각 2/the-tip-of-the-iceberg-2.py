n = int(input())
heights = list(int(input()) for _ in range(n))

max_cnt = 0
for i in range(1, 1000):
    cnt = 0
    hs = heights.copy()
    hs = [h - i for h in hs]
    for j in range(n-1):
        if hs[j] <= 0 and hs[j+1] > 0:
            cnt += 1
        elif hs[j] > 0 and hs[j+1] <= 0:
            cnt += 1
        else:
            cnt -= 1
    max_cnt = max(max_cnt, cnt)
print(max_cnt)