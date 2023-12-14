arr = list(map(int, input().split()))
cnt = 0
arr1 = arr.copy()
arr2 = arr.copy()
for _ in range(100):
    cnt += 1
    min_val = min(arr[0], arr[-1])
    max_val = max(arr[0], arr[-1])
    min_idx = arr.index(min_val)
    max_idx = arr.index(max_val)
    arr1[min_idx], arr1[1] = arr1[1], arr1[min_idx]
    arr2[max_idx], arr2[1] = arr2[1], arr2[max_idx]
    
    if arr1 == sorted(arr1) or arr2 == sorted(arr2):
        break

print(cnt)