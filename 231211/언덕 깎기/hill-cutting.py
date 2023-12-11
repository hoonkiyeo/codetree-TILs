n = int(input())
arr = [int(input()) for _ in range(n)]

min_cost = float('inf')
for min_h in range(84):  # 0부터 83까지
    max_h = min_h + 17
    cost = 0
    for k in range(n):
        if arr[k] < min_h:
            cost += (min_h - arr[k]) ** 2
        elif arr[k] > max_h:
            cost += (arr[k] - max_h) ** 2
    min_cost = min(min_cost, cost)

print(min_cost)