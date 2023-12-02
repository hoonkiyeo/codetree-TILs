n,h,t = map(int, input().split())
arr = list(map(int, input().split()))


min_diff = 999
for i in range(n-t+1):
    diff = 0
    arr2 = arr[i:i+t]
    for ele in arr2:
        diff += abs(h - ele)
    min_diff = min(min_diff, diff)
print(min_diff)