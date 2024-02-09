n,m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

# 마름모 넓이
def get_area(k):
    return k**2 + (k+1)**2

# 채굴 가능한 금의 개수 (row, col이 중심인)
def get_gold(row, col, k):
    s = arr[row][col]
    for i in range(n):
        for j in range(n):
            if i == row and j == col:
                continue
            # i,j인 지점이 마름모에 포함이 되는 조건
            if abs(row-i) + abs(col-j) <= k:
                s += arr[i][j]
    return s

# 완전 탐색
max_cnt = 0
for row in range(n):
    for col in range(n):
        # max_k 범위 설정
        for k in range(2*n-1):
            cnt = get_gold(row, col, k)
            if cnt * m >= get_area(k):
                max_cnt = max(max_cnt, cnt)
print(max_cnt)