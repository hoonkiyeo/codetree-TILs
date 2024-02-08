n,m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
cnt = 0

if m == 1:
    print(n*2)
else:
    def is_happy_arr(seq, m):
        max_cnt = 1
        consecutive_cnt = 1

        for i in range(len(seq)-1):
            if seq[i] != seq[i+1]:
                consecutive_cnt = 1
            consecutive_cnt += 1
            max_cnt = max(max_cnt, consecutive_cnt)
        
        if max_cnt < m:
            return False
        return True

    for row in arr:
        if is_happy_arr(row, m):
            cnt += 1
    for col in range(len(arr)):
        arr_col = []
        for row in range(len(arr)):
            arr_col.append(arr[row][col])
        if is_happy_arr(arr_col, m):
            cnt += 1
    print(cnt)