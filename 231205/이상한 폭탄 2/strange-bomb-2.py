n,k = map(int, input().split())
bombs = [int(input()) for _ in range(n)]
bombs.sort()


max_bomb = 0
for i in range(n):
    for j in range(i+1, n):
        if j - i > 3:
            continue
        if bombs[i] == bombs[j]:
            max_bomb = max(max_bomb, bombs[i])

print(max_bomb)