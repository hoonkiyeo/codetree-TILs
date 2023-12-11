n,k = map(int, input().split())
arr = [int(input()) for _ in range(n)]

max_num = 1000000
arr_bomb = [0] * (max_num+1)
ans = 0

for i in range(n):
    for j in range(i+1,n):
        if j-i <= k and arr[i] == arr[j]:
            arr_bomb[arr[i]] += 1

max_cnt = max(arr_bomb)

if max_cnt == 0:
    print(max_cnt)
else:
    for i in range(max_num, -1, -1):
        if arr_bomb[i] == max_cnt:
            ans = i
            break
    print(ans)