n,m = map(int, input().split())
pos = list(map(int, input().split()))

def min_wifi(n,m,arr):
    i == 0
    cnt = 0

    while i < n:
        if arr[i] == 1:
        # 만약 사람이 살고 있는 위치라면
            cnt += 1
            i += 2*m+1
        else:
            i += 1
    
    return cnt

print(cnt)