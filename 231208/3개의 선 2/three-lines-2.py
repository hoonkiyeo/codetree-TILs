n = int(input())
coords = []
for _ in range(n):
    x,y = map(int, input().split())
    coords.append((x,y))

def check():
    xys = [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]]
    for i in range(0, 11):
        for j in range(0, 11):
            for k in range(0, 11):
                for xy1, xy2, xy3 in xys:
                    stoppoint = True
                    for point in coords:
                        if point[xy1] == i or point[xy2] == j or point[xy3] == k:
                            continue
                        stoppoint = False
                    if stoppoint:
                        return 1
    return 0
print(check())