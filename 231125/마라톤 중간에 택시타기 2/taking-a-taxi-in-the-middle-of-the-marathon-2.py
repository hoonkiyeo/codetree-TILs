import sys
n = int(input())
path = []
min_dist = sys.maxsize
for _ in range(n):
    x,y = map(int, input().split())
    path.append((x,y))

# for i in range(1,len(path)-1):
#     dist = 0
#     paths.pop(i)
#     for j in range(len(paths)-1):
#         x = abs(paths[j][0] - paths[j+1][0])
#         y = abs(paths[j][1] - paths[j+1][1])
#         dist += x+y
#     if dist < min_dist:
#         min_dist = dist
#     paths = path

# print(min_dist)

def calculate_min_distance(path):
    # Step 1: Calculate the total distance of the original path
    total_dist = sum(abs(path[i][0] - path[i+1][0]) + abs(path[i][1] - path[i+1][1]) for i in range(len(path) - 1))

    # Step 2: Find the maximum distance saved by removing each point
    max_saved_dist = 0
    for i in range(1, len(path) - 1):
        # Distance from previous point to current point
        dist_prev_to_curr = abs(path[i][0] - path[i-1][0]) + abs(path[i][1] - path[i-1][1])
        # Distance from current point to next point
        dist_curr_to_next = abs(path[i][0] - path[i+1][0]) + abs(path[i][1] - path[i+1][1])
        # Distance from previous point to next point if current is removed
        dist_prev_to_next = abs(path[i+1][0] - path[i-1][0]) + abs(path[i+1][1] - path[i-1][1])
        # Distance saved by removing the current point
        saved_dist = dist_prev_to_curr + dist_curr_to_next - dist_prev_to_next
        max_saved_dist = max(max_saved_dist, saved_dist)

    # Step 3: Calculate the minimum distance after removing the point that saves the maximum distance
    min_dist = total_dist - max_saved_dist
    return min_dist

# Example usage
print(calculate_min_distance(path))