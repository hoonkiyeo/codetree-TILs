n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

max_cnt = 0
second_max_cnt = 0
max_idx = (-1, -1)

for i in range(n):
    for j in range(n - 2):
        current_sum = arr[i][j] + arr[i][j+1] + arr[i][j+2]

        # Check for overlap with current max
        if max_idx[0] == i and max_idx[1] - 2 <= j <= max_idx[1] + 2:
            if current_sum > second_max_cnt:
                second_max_cnt = current_sum
        else:
            if current_sum > max_cnt:
                second_max_cnt = max_cnt
                max_cnt = current_sum
                max_idx = (i, j)
            elif current_sum > second_max_cnt:
                second_max_cnt = current_sum

print(max_cnt + second_max_cnt)