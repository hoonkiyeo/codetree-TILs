n = int(input())
arr = [int(input()) for _ in range(n)]

min_cost = 999999
for i in range(n):
    for j in range(i+1,n):
        max_h = max(arr[i], arr[j])
        min_h = min(arr[i], arr[j])
        cost = 0
        if max_h - min_h > 17:
            continue
        for k in range(n):
            if k == i or k == j:
                continue
            if arr[k] < min_h:
                cost += (min_h - arr[k]) * (min_h - arr[k])
            elif arr[k] > max_h:
                cost += (arr[k] - max_h) * (arr[k] - max_h)
        min_cost = min(min_cost, cost)
print(min_cost)