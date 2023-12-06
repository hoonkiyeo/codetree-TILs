x,y = map(int, input().split())

cnt = 0
for i in range(x,y+1):
    s = str(i)
    if s == s[::-1]:
        cnt += 1
print(cnt)