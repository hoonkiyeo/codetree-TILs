t,a,b = map(int, input().split())
arr = [0] * (b+1)

for _ in range(t):
    c,x = input().split()
    x = int(x)
    arr[x] = c

s_indices = [i for i in range(a, b+1) if arr[i] == 'S']
n_indices = [i for i in range(a, b+1) if arr[i] == 'N']
special_cnt = 0

for i in range(a,b+1):
    closest_s = min([abs(i-s) for s in s_indices])
    closest_n = min([abs(i-n) for n in n_indices])

    if closest_s <= closest_n:
        special_cnt += 1
print(special_cnt)