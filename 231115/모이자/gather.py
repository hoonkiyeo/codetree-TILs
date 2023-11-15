import sys
n = int(input())
arr = list(map(int, input().split()))


min_dist = sys.maxsize
for i in range(len(arr)):
    dist = 0
    for j in range(len(arr)):
        idx = abs(i-j)
        dist += arr[j] * idx
    min_dist = min(min_dist, dist)
print(min_dist)