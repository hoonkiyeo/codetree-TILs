n = int(input())
seats = [*input()]

max_dist = 0
for i in range(n):
    if seats[i] == '1':
        continue
    dist = float('inf')
    indices = [
        j for j in range(n)
        if seats[j] == '1' or i == j
    ]

    for j in range(len(indices)-1):
        dist = min(dist, (abs(indices[j] - indices[j+1])))
    
    max_dist = max(max_dist, dist)
print(max_dist)