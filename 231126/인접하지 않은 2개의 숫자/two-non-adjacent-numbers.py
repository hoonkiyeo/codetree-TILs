n = int(input())
nums = list(map(int, input().split()))
max_n = 0

for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        if abs(i-j) != 1:
            num = nums[i] + nums[j]
            if num > max_n:
                max_n = num
print(max_n)