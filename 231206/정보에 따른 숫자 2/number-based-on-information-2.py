t,a,b = map(int, input().split())
pos = []
for _ in range(t):
    c,x = input().split()
    x = int(x)
    pos.append((c,x))

s_indices = [x for a,x in pos if a == 'S']
n_indices = [x for a,x in pos if a == 'N']
special_cnt = 0

for i in range(a,b+1):
    closest_s = min([abs(i-s) for s in s_indices])
    closest_n = min([abs(i-n) for n in n_indices])
    if closest_s <= closest_n:
        special_cnt += 1

print(special_cnt)