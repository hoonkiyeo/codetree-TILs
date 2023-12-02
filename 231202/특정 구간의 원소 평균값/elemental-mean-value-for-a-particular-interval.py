n = int(input())
nums = list(map(int, input().split())) 

cnt = 0
for i in range(n):
    for j in range(i, n):
        avg = sum(nums[i:j+1]) / len(nums[i:j+1])
        if avg in nums[i:j+1]:
            cnt += 1
print(cnt)