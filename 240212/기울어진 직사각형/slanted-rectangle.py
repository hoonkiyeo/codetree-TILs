n = int(input())
arr = [list(map(int, input().split( ))) for _ in range(n)]

def in_range(row, col):
    return 0 <= row < n and 0 <= col < n

def get_score(row, col, k, l):
    dxs, dys = [-1, -1, 1, 1], [1, -1, -1, 1]
    moves = [k, l, k, l]

    total_score = 0
    for dx, dy, move in zip(dxs, dys, moves):
        for _ in range(move):
            row = row + dx
            col = col + dy

            if not in_range(row,col):
                return 0
            
            total_score += arr[row][col]
    
    return total_score

max_score = 0
for row in range(n):
    for col in range(n):
        for k in range(1, n):
            for l in range(1, n):
                if k == l:
                    continue
                max_score = max(max_score, get_score(row, col, k, l))

print(max_score)