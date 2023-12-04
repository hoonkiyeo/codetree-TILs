n,b = map(int, input().split())
price = []
for _ in range(n):
    p = int(input())
    price.append(p)
price.sort()

max_cnt = 0
for i in range(n):
    total_price = 0
    cnt = 0
    p = price[i] // 2
    total_price += p
    cnt += 1
    for j in range(n):
        if i == j:
            continue
        if total_price + price[j] > b:
            break
        else:
            total_price += price[j]
            cnt += 1
    max_cnt = max(max_cnt, cnt)
print(max_cnt)