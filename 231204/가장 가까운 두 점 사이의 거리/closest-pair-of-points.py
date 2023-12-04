n = int(input())
coords = []
for _ in range(n):
    x,y = map(int, input().split())
    coords.append((x,y))

min_dist = 9999999
idx = (0,0)
for i in range(n):
    for j in range(i+1, n):
        if i == j:
            continue
        x1,y1 = coords[i][0], coords[i][1]
        x2,y2 = coords[j][0], coords[j][0]
        dist = abs(x1-x2) + abs(y1-y2)
        if dist < min_dist:
            min_dist = dist
            idx = (i,j)

i,j = idx[0], idx[1]
x1,y1 = coords[i][0], coords[i][1]
x2,y2 = coords[j][0], coords[j][1]
s_dist = abs(x1-x2) * abs(x1-x2) + abs(y1-y2) * abs(y1-y2)
print(s_dist)