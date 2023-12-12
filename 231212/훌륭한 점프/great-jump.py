n, k = map(int, input().split())
arr = list(map(int, input().split()))

def is_possible(max_val):
    last_idx = 0
    for i in range(1, n):
        if arr[i] <= max_val:
            if i - last_idx > k:
                return False
            last_idx = i
    return True

for i in range(max(arr[0], arr[n-1]), max_num + 1):
    if is_possible(i):
        print(i)
        break