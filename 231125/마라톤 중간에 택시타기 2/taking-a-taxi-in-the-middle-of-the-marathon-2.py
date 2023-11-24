import sys
n = int(input())
path = []
min_dist = sys.maxsize
for _ in range(n):
    x,y = map(int, input().split())
    path.append((x,y))

total_dist = sum(abs(path[i][0] - path[i+1][0]) + abs(path[i][1] - path[i+1][1]) for i in range(len(path) - 1))
max_saved_dist = 0
for i in range(1, len(path)-1):
    prev_to_curr = abs(path[i][0] - path[i-1][0]) + abs(path[i][1] - path[i-1][1])
    curr_to_next = abs(path[i][0] - path[i+1][0]) + abs(path[i][1] - path[i+1][1])
    prev_to_next = abs(path[i+1][0] - path[i-1][0]) + abs(path[i+1][1] - path[i-1][1])
    saved_dist = prev_to_curr + curr_to_next - prev_to_next
    max_saved_dist = max(max_saved_dist, saved_dist)
min_dist = total_dist - max_saved_dist
print(min_dist)