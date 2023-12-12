n = int(input())
segments = []
arr = [0] * 101
for _ in range(n):
    x1,x2 = map(int, input().split())
    segments.append((x1,x2))

for segment in segments:
    x1,x2 = segment[0], segment[1]
    for i in range(x1,x2+1):
        arr[i] += 1

if n in arr:
    print('Yes')
else:
    print('No')