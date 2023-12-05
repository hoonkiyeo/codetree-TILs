n,b = map(int, input().split())
presents = []
for _ in range(n):
    p,s = map(int, input().split())
    presents.append((p,s))
presents = sorted(presents, key=lambda x:x[0]+x[1])

max_cnt = 0
for i in range(n):
    cnt = 0
    total = 0
    p,s = presents[i]
    p = p // 2
    total += (p+s)
    cnt += 1

    for j in range(n):
        if i == j:
            continue
        p,s = presents[j]
        total += (p+s)
        cnt += 1
        if total == b:
            break
        elif total > b:
            cnt -= 1
            break
    max_cnt = max(max_cnt, cnt)
print(max_cnt)