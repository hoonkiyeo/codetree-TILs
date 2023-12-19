n,m = map(int, input().split())
pos = list(map(int, input().split()))
cnt = 0

# 2*m+1
for i in range(0, n, 2*m+1):
    if 1 in pos[i:i+(2*m+1)]:
        cnt += 1
print(cnt)