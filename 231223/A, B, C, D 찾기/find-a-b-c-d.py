nums = list(map(int, input().split()))
nums.sort()
max_n = max(nums)
a = nums[0]
b = nums[1]
C = [num for num in nums[2:] if b <= num <= a+b]
val1 = 0
val2 = 0
for c in C:
    d = max_n-a-b-c
    if d >= c:
        if a+d in nums and b+d in nums and c+d in nums and a+b+d in nums and a+c+d in nums and b+c+d in nums and a+b+c+d in nums:
            val1 = c
            val2 = d

print(a,b,val1,val2)