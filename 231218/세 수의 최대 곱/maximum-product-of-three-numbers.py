n = int(input())
nums = list(map(int, input().split()))

max_mul = 0

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            val = nums[i] * nums[j] * nums[k]
            max_mul = max(max_mul, val)
print(max_mul)