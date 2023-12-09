n,m = map(int, input().split())
pairs = []
for _ in range(m):
    a,b = map(int, input().split())
    pairs.append((a,b))

max_cnt = 0
for i in range(m):
    x,y = pairs[i]
    cnt = 1
    for j in range(i+1, m):
        x2,y2 = pairs[j]
        if (x == x2 and y == y2) or (x == y2 and y == x2):
            cnt += 1
    max_cnt = max(max_cnt, cnt)
print(max_cnt)