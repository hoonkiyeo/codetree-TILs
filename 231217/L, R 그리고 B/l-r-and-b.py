# L -> B

# B: 4,3
# L: 9,6
# R: 6,6
# -> 7

# B: 2,3
# L: 8,2
# R: 5,2
# -> 6
from collections import deque

def bfs(grid, start, end, block):
    rows, cols = len(grid), len(grid[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    queue = deque([(start, 0)])  # (position, distance)
    visited[start[0]][start[1]] = True

    while queue:
        (x, y), dist = queue.popleft()
        if (x, y) == end:
            return dist - 1  # Subtract 1 because L and B are not counted

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and not visited[nx][ny] and grid[nx][ny] != block:
                visited[nx][ny] = True
                queue.append(((nx, ny), dist + 1))

    return -1  # Path not found

def find_positions(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'L':
                start = (i, j)
            elif grid[i][j] == 'B':
                end = (i, j)
    return start, end

def main(grid):
    start, end = find_positions(grid)
    return bfs(grid, start, end, 'R')

# 사용자로부터 격자 입력 받기
grid = []
for _ in range(10):
    row = input()
    grid.append(row)

# 결과 출력
print(main(grid))