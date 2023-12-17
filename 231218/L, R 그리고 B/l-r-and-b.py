arr = []
n = 10
for _ in range(n):
    row = input()
    arr.append(row)

idx_b = (0,0)
idx_l = (0,0)
idx_r = (0,0)
for i in range(n):
    for j in range(n):
        if arr[i][j] == 'B':
            idx_b = (i,j)
        elif arr[i][j] == 'L':
            idx_l = (i,j)
        elif arr[i][j] == 'R':
            idx_r = (i,j)

min_dist = min_dist = abs(idx_b[0] - idx_l[0]) + abs(idx_b[1] - idx_l[1]) - 1

if idx_b[0] < idx_r[0] < idx_l[0] or idx_l[0] < idx_r[0] < idx_b[0]:
    if idx_b[1] == idx_l[1] == idx_r[1]:
        min_dist = abs(idx_b[0] - idx_l[0]) + abs(idx_b[1] - idx_l[1]) + 1
elif idx_b[1] < idx_r[1] < idx_l[1] or idx_l[1] < idx_r[1] < idx_b[1]:
    if idx_b[0] == idx_l[0] == idx_r[0]:
        min_dist = abs(idx_b[0] - idx_l[0]) + abs(idx_b[1] - idx_l[1]) + 1

print(min_dist)