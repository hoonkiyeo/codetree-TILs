n = int(input())
nums = list(map(int, input().split()))

# 홀 + 홀 = 짝
# 짝 + 홀 = 홀
# 짝 + 짝 = 짝

even = 0
odd = 0
for num in nums:
    # 짝수와 홀수 카운트
    if (num % 2 == 0):
        even += 1
    else:
        odd += 1

group_cnt = 0
while True:
    if group_cnt % 2 == 0:
        # 짝수 묶음을 만들어야할 경우: 짝수 1개 또는 홀수 2개
        if even:
            even -= 1
            group_cnt += 1
        elif odd >= 2:
            odd -= 2
            group_cnt += 1
        else:
            if even > 0 or odd > 0:
                group_cnt -= 1
            break
    else:
        # 홀수 묶음을 만들어야할 경우: 홀수 1개
        if odd:
            odd -= 1
            group_cnt += 1
        else:
            break
print(group_cnt)