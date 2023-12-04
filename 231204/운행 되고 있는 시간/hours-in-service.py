n = int(input())
times = []
for _ in range(n):
    start, end = map(int, input().split())
    times.append((start,end))

max_time = 0
for i in range(n):
    arr = [0] * 1001
    for j in range(n):
        if i == j:
            continue
        a,b = times[j][0], times[j][1]
        for k in range(a,b):
            arr[k] = 1
    max_time = max(max_time, sum(arr))
print(max_time)