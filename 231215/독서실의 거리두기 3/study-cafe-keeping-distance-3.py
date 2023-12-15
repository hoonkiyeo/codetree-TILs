n = int(input())
seats = [*input()]


max_dist = 0
for i in range(n):
    if seats[i] == '1':
        continue
    
    indices = [
        j for j in range(n) if seats[j] == '1' or i == j
    ]
    min_dist = float('inf')

    for j in range(len(indices)-1):
        min_dist = min(min_dist, abs(indices[j] - indices[j+1]))

    max_dist = max(min_dist, max_dist)

print(max_dist)


# 0 1 4 7 11