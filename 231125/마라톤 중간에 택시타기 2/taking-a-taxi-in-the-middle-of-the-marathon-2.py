import sys
n = int(input())
path = []
min_dist = sys.maxsize
for _ in range(n):
    x,y = map(int, input().split())
    path.append((x,y))
paths = path.copy()


for i in range(1,len(path)-1):
    dist = 0
    paths.pop(i)
    for j in range(len(paths)-1):
        x = abs(paths[j][0] - paths[j+1][0])
        y = abs(paths[j][1] - paths[j+1][1])
        dist += x+y
    if dist < min_dist:
        min_dist = dist
    paths = path

print(min_dist)