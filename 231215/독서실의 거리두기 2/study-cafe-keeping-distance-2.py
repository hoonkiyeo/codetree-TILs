n = int(input())
pos = [*input()]

max_dist = 0
for i in range(n):
    if pos[i] == '1':
        continue
    dist = float('inf')
    indices = [j for j in range(n) if pos[j] == '1' or j == i]
    size = len(indices)

    for j in range(size-1):
        dist = min(dist, abs(indices[j]-indices[j+1]))
    max_dist = max(dist, max_dist)
print(max_dist)