n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))

max_n = 0
for i in range(len(nums)-2):
    for j in range(i+1, len(nums)-1):
        for k in range(j+1, len(nums)):
            x=nums[i]; y=nums[j]; z=nums[k]
            if int(str(x // 1)[-1]) + int(str(y // 1)[-1]) + int(str(z // 1)[-1]) < 10:
                if int(str(x // 10)[-1]) + int(str(y // 10)[-1]) + int(str(z // 10)[-1]) < 10:
                    if int(str(x // 100)[-1]) + int(str(y // 100)[-1]) + int(str(z // 100)[-1]) < 10:
                        if int(str(x // 1000)[-1]) + int(str(y // 1000)[-1]) + int(str(z // 1000)[-1]) < 10:
                            if int(str(x // 10000)[-1]) + int(str(y // 10000)[-1]) + int(str(z // 10000)[-1]) < 10:
                                num = x+y+z
                                if num > max_n:
                                    max_n = num
print(max_n)