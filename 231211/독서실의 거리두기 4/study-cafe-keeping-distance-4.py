n = int(input())
seats = [*input()]

max_dist = 0
for i in range(n):
    for j in range(i+1, n):
        if seats[i] == '1' or seats[j] == '1':
            continue
        dist = float('inf')
        indices = [
            k for k in range(n)
            if seats[k] == '1' or k == i or k == j
        ]

        for k in range(len(indices)-1):
            dist = min(dist, abs(indices[k] - indices[k+1]))
        
        max_dist = max(max_dist, dist)
print(max_dist)