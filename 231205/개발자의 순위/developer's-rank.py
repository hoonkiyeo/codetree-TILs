k,n = map(int, input().split())
rk = []
for _ in range(k):
    rk.append(list(map(int, input().split())))

pairs = {}
for r in rk:
    for i in range(n):
        for j in range(i+1, n):
            comb = (r[i],r[j])
            if comb in pairs:
                pairs[comb] += 1
            else:
                pairs[comb] = 1

cnt = 0
for v in pairs.values():
    if v == k:
        cnt += 1
print(cnt)