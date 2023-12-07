n = int(input())
nums = list(map(int ,input().split()))

min_sum = 9999
for i in range(n):
    nums[i] *= 2
    
    for j in range(n):
        remaining_arr = []
        for k, ele in enumerate(nums):
            if k != j:
                remaining_arr.append(ele)
        sum_diff = 0
        for k in range(len(remaining_arr)-1):
            sum_diff += abs(remaining_arr[k] - remaining_arr[k+1])
        min_sum = min(sum_diff, min_sum)
    
    nums[i] //= 2

print(min_sum)