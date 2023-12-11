n,k = map(int, input().split())
arr = list(map(int, input().split()))
max_n = 10000


min_cost = float('inf')
for i in range(1, max_n+1):
    # 최솟값 탐색
    cost = 0
    for j in range(n):
        if arr[j] >= i and arr[j] - i <= k:
            continue
        elif arr[j] < i:
            cost += i - arr[j]
        else:
            cost += arr[j] - (i+k)
    min_cost = min(min_cost, cost)

print(min_cost)