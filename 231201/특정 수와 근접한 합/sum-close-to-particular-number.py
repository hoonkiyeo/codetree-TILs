n,s = map(int, input().split())
arr = list(map(int, input().split()))

min_diff = 99999
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        curr_sum = sum(arr) - arr[i] - arr[j]
        if abs(s - curr_sum) < min_diff:
            min_diff = abs(s-curr_sum)
print(min_diff)