n,k = map(int, input().split())
bombs = [int(input()) for _ in range(n)]
bombs.sort()


bombs_in_danger = []
for i in range(n):
    for j in range(i+1, n):
        if j - i > 3:
            continue
        if bombs[i] == bombs[j]:
            bombs_in_danger.append(bombs[i])
print(max(bombs_in_danger))