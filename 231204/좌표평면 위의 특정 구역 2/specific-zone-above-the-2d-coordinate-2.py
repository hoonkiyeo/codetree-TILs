n = int(input())
coords = []

for _ in range(n):
    x,y = map(int, input().split())
    coords.append((x,y))


for i in range(n):
    min_area = 999999999999999999
    min_x = 40001
    max_x = 0
    min_y = 40001
    max_y = 0
    for j in range(n):
        if i == j:
            continue
        x,y = coords[j][0], coords[j][1]
        min_x = min(min_x, x)
        max_x = max(max_x, x)
        min_y = min(min_y, y)
        max_y = max(max_y, y)
    area = (max_x - min_x) * (max_y - min_y)
    min_area = min(min_area, area)
print(min_area)