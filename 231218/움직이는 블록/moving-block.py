n = int(input())
cost = 0
arr = [int(input()) for _ in range(n)]
threshold = sum(arr) // n

for i in range(n):
    if arr[i] <= threshold:
        continue
    cost += arr[i] - threshold
print(cost)