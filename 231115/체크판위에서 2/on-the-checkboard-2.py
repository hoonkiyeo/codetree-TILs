r,c = map(int, input().split())
arr = []
for _ in range(r):
    arr.append(list(input().split()))

cnt = 0
start = arr[0][0]
end = arr[r-1][c-1]
if start == end:
    print(cnt)
else:
    paths = []
    for i in range(1, r-1):
        for j in range(1, c-1):
            if start != arr[i][j]:
                paths.append((i,j))
    for x,y in paths:
        for i in range(x+1, r-1):
            for j in range(y+1, c-1):
                if arr[x][y] != arr[i][j]:
                    cnt += 1
    print(cnt)