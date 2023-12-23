nums = list(map(int, input().split()))
nums.sort()
n = len(nums)
a,b,c = 0,0,0
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            A = nums[i]
            B = nums[j]
            C = nums[k]
            if A+B in nums and B+C in nums and A+C in nums and A+B+C in nums:
                a = A
                b = B
                c = C
                break
print(a,b,c)