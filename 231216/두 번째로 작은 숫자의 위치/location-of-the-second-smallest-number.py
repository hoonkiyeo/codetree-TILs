n = int(input())
nums = list(map(int, input().split()))
set_num = sorted(list(set(nums)))

if len(set_num) == 1 or nums.count(set_num[1]) > 1:
    print(-1)
else:
    print(nums.index(set_num[1])+1)