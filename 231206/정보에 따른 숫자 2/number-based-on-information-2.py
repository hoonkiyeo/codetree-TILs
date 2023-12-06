t,a,b = map(int, input().split())
arr = [0] * (b+1)

for _ in range(t):
    c,x = input().split()
    x = int(x)
    arr[x] = c

s_indices = [i for i in range(1, b+1) if arr[i] == 'S']
n_indices = [i for i in range(1, b+1) if arr[i] == 'N']
cnt = 0
if 'N' not in arr:
    print(b)
else:
    for i in range(1, b+1):
        dist_to_s = []
        dist_to_n = []
        for j in s_indices:
            dist_to_s.append(abs(i-j))
        for j in n_indices:
            dist_to_n.append(abs(i-j))
        if min(dist_to_s) <= min(dist_to_n):
            cnt += 1
    print(cnt)