n,k = map(int, input().split())
nums = list(map(int, input().split()))

max_sum = 0
for i in range(n - k + 1):
    val_sum = 0
    for j in range(i, i+k):
        val_sum += nums[j]
    if val_sum > max_sum:
        max_sum = val_sum
print(max_sum)