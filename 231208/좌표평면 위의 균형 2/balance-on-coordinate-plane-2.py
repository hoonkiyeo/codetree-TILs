n = int(input())
points = []
for _ in range(n):
    x,y = map(int, input().split())
    points.append((x,y))




minimax = 100
for i in range(0, 101, 2):
    for j in range(0, 101, 2):
        qudrant1 = 0
        qudrant2 = 0
        qudrant3 = 0
        qudrant4 = 0
        for x,y in points:
            if (x < i and y > j):
                qudrant1 += 1
            elif (x < i and y < j):
                qudrant4 += 1
            elif (x > i and y > j):
                qudrant2 += 1
            elif (x > i and y < j):
                qudrant3 += 1
        max_points = max(qudrant1, qudrant2, qudrant3, qudrant4)
        minimax = min(max_points, minimax)
print(minimax)