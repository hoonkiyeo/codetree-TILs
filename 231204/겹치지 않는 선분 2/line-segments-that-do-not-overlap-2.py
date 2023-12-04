n = int(input())
coords = []
for _ in range(n):
    x1,x2 = map(int, input().split())
    coords.append((x1, x2))

total_cnt = 0
for i in range(n):
    x1,x2 = coords[i]
    cnt = 0
    for j in range(n):
        if i == j:
            continue
        x3,x4 = coords[j]
        if (x1 < x3 and x2 > x4) or (x1 > x3 and x2 < x4):
            cnt += 1
    if cnt == 0:
        total_cnt += 1
print(total_cnt)