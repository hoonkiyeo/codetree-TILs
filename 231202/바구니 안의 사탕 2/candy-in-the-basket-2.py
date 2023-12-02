n,k = map(int, input().split())
positions = [0] * 101
max_pos = 0
for _ in range(n):
    c,i = map(int, input().split())
    positions[i] += c
    max_pos = max(i, max_pos)

max_cnt = 0
for i in range(1, max_pos-k*2+1):
    cnt = sum(positions[i:i+k*2+1])
    max_cnt = max(cnt, max_cnt)
print(max_cnt)