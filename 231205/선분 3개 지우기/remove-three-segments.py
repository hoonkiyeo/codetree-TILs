n = int(input())
coords = []
for _ in range(n):
    x1,x2 = map(int, input().split())
    coords.append((x1,x2))

total_cnt = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            arr = [0] * 101
            is_bool = True
            for l in range(n):
                if l != i and l != j and l != k:
                    x1,x2 = coords[l][0], coords[l][1]
                    for m in range(x1, x2+1):
                        arr[m] += 1  
            for ele in arr:
                if ele > 1:
                    is_bool = False
            if is_bool:
                total_cnt += 1
print(total_cnt)