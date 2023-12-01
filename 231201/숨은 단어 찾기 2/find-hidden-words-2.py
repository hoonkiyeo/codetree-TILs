n,m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(input())
cnt = 0

def in_range(x,y):
    return x >= 0 and y >= 0 and x < n and y < m

for i in range(n):
    for j in range(m):
        if arr[i][j] == 'L':
            # check right
            if in_range(i, j+1) and in_range(i, j+2):
                if arr[i][j+1] == 'E' and arr[i][j+2] == 'E':
                    cnt += 1
            # check left
            if in_range(i, j-1) and in_range(i, j-2):
                if arr[i][j-1] == 'E' and arr[i][j-2] == 'E':
                    cnt += 1
            # check down
            if in_range(i+1, j) and in_range(i+2, j):
                if arr[i+1][j] == 'E' and arr[i+2][j] == 'E':
                    cnt += 1
            # check up
            if in_range(i-1, j) and in_range(i-2, j):
                if arr[i-1][j] == 'E' and arr[i-2][j] == 'E':
                    cnt += 1
            # check down-right
            if in_range(i+1,j+1) and in_range(i+2, j+2):
                if arr[i+1][j+1] == 'E' and arr[i+2][j+2] == 'E':
                    cnt += 1
            # check down-left
            if in_range(i+1, j-1) and in_range(i+2, j-2):
                if arr[i+1][j-1] == 'E' and arr[i+2][j-2] == 'E':
                    cnt += 1
            # check up-right
            if in_range(i-1,j+1) and in_range(i-2, j+2): 
                if arr[i-1][j+1] == 'E' and arr[i-2][j+2] == 'E':
                    cnt += 1
            # check up-left
            if in_range(i-1,j-1) and in_range(i-2, j-2):
                if arr[i-1][j-1] == 'E' and arr[i-2][j-2] == 'E':
                    cnt += 1
print(cnt)