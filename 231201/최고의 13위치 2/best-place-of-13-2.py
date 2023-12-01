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
        curr = arr[i][j] + arr[i][j+1] + arr[i][j+2]
        if curr > max_cnt:
            max_cnt = curr
            idx = (i,j)

# second max_cnt
for i in range(n):
    for j in range(n-2):
        if i == idx[0] and idx[1] - 2 <= j <= idx[1] + 2:
            continue 
        curr = arr[i][j] + arr[i][j+1] + arr[i][j+2]
        if curr > max_cnt2:
            max_cnt2 = curr
print(max_cnt + max_cnt2)