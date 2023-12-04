n = int(input())
coords = []
for _ in range(n):
    x,y = map(int, input().split())
    coords.append((x,y))

min_dist_squared = 9999999999
for i in range(n):
    for j in range(i + 1, n):
        x1, y1 = coords[i]
        x2, y2 = coords[j]
        dist_squared = (x1 - x2) ** 2 + (y1 - y2) ** 2
        if dist_squared < min_dist_squared:
            min_dist_squared = dist_squared

print(min_dist_squared)