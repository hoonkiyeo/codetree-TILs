n = int(input())
ranges = []

for _ in range(n):
    x,y = map(int, input().split())
    ranges.append((x,y))

ans = 0

for i in range(1, 10001):
    is_bool = True
    num = i
    for x,y in ranges:
        num *= 2
        if not x <= num <= y:
            is_bool = False
    if is_bool:
        ans = i
        break
print(ans)