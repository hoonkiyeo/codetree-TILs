n = int(input())
segments = []
for _ in range(n):
    x1,x2 = map(int, input().split())
    segments.append((x1,x2))

is_possible = False
for i in range(n):
    arr = [0] * 101
    for j in range(n):
        if i == j:
            continue
        x1,x2 = segments[j][0], segments[j][1]
        for k in range(x1,x2+1):
            arr[k] += 1
    if n-1 in arr:
        is_possible = True
    if is_possible:
        break

if is_possible:
    print('Yes')
else:
    print('No')