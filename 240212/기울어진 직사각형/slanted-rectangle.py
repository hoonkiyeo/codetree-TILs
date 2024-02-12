n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

def in_range(row, col):
    return 0 <= row < n and 0 <= col < n

def get_sum(row, col, k, l):
    # 1 -> 2 -> 3 -> 4
    dxs, dys = [-1, -1, 1, 1], [1, -1, -1, 1]
    move_nums = [k,l,k,l]
    val_sum = 0

    for dx, dy, move_num in zip(dxs, dys, move_nums):
        for _ in range(move_num):
            row, col = row + dx, col + dy

            if not in_range(row,col):
                return 0

            val_sum += arr[row][col]

    return val_sum

ans = 0

for row in range(n):
    for col in range(n):
        for k in range(1, n):
            for l in range(1, n):
                ans = max(ans, get_sum(row, col, k, l))

print(ans)