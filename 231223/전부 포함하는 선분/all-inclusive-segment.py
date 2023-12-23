n = int(input())
segments = []
arr = [0] * 101
for _ in range(n):
    x1,x2 = map(int, input().split())
    segments.append((x1,x2))

min_length = float('inf')
for i in range(n):
    length = 0
    arr = [0] * 101
    min_k = float('inf')
    max_k = 0
    for j in range(n):
        if j == i:
            continue
        x1,x2 = segments[j]
        for k in range(x1,x2+1):
            arr[k] = 1
            min_k = min(min_k, k)
            max_k = max(max_k, k)
    length = max_k - min_k
    min_length = min(min_length, length)
print(min_length)