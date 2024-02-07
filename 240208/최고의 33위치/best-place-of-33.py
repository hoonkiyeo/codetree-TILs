n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
max_cnt = 0

# helper function
def get_coins(row_s, row_e, col_s, col_e):
    cnt = 0

    for row in range(row_s, row_e+1):
        for col in range(col_s, col_e+1):
            cnt += arr[row][col]
    
    return cnt

# 0 1 2
for row in range(n):
    for col in range(n):
        # 범위를 벗어나는 경우 제외
        if  row + 2 >= n or col + 2 >= n:
            continue
        
        # 해당 범위 안의 동전 수 카운트
        cnt = get_coins(row, row+2, col, col+2)

        # 최대 동전 수 갱신
        max_cnt = max(max_cnt, cnt)

print(max_cnt)