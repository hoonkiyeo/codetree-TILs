n,m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
total = 0

def in_range(row,col):
    return row >= 0 and col >= 0 and col < m and row < n

case_1 = 0
case_2 = 0
case_3 = 0
case_4 = 0
case_5 = 0
case_6 = 0
for row in range(n):
    for col in range(m):
        # case1
        if in_range(row,col) and in_range(row+1, col) and in_range(row+1, col+1):
            case_1 = arr[row][col] + arr[row+1][col] + arr[row+1][col+1]
        # case2
        if in_range(row,col) and in_range(row+1, col) and in_range(row+1, col-1):
            case_2 = arr[row][col] + arr[row+1][col] + arr[row+1][col-1]
        # case3
        if in_range(row,col) and in_range(row, col-1) and in_range(row+1, col-1):
            case_3 = arr[row][col] + arr[row][col-1] + arr[row+1][col-1]
        # case4
        if in_range(row,col) and in_range(row, col+1) and in_range(row+1, col+1):
            case_4 = arr[row][col] + arr[row][col+1] + arr[row+1][col+1]
        # case5
        if in_range(row,col) and in_range(row, col+1) and in_range(row, col+2):
            case_5 = arr[row][col] + arr[row][col+1] + arr[row][col+2]
        # case6
        if in_range(row,col) and in_range(row+1, col) and in_range(row+2, col):
            case_6 = arr[row][col] + arr[row+1][col] + arr[row+2][col]
        
        total = max(total, case_1, case_2, case_3, case_4, case_5, case_6)

print(total)