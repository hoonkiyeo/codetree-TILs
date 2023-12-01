n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

max_cnt = 0
max_cnt2 = 0
idx = 0
# max_cnt
for i in range(n):
    for j in range(n-2):
        cnt = 0
        cnt += (arr[i][j] + arr[i][j+1] + arr[i][j+2])
        if cnt > max_cnt:
            max_cnt = cnt
            idx = (i,j)
# second max_cnt
for i in range(n):
    for j in range(n-2):
        cnt = 0
        if (i == idx[0] and j == idx[1]) or j == idx[1]-1 or j == idx[1]-2 or j == idx[1]+1 or j == idx[1]+2:
            continue 
        cnt += (arr[i][j] + arr[i][j+1] + arr[i][j+2])
        if cnt > max_cnt2:
            max_cnt2 = cnt
print(max_cnt + max_cnt2)