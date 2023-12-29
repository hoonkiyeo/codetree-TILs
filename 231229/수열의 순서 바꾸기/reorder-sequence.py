n = int(input())
nums = list(map(int, input().split()))
cnt = 0

for i in range(n):
    for j in range(i+1, n):
        if nums[j] > nums[j-1]:
            continue
        else:
            cnt += 1
            break

print(cnt)