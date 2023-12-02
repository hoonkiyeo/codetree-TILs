stats = list(map(int, input().split()))
total_stats = sum(stats)

min_diff = 1000000
for i in range(len(stats)):
    for j in range(i+1, len(stats)):
        for k in range(j+1, len(stats)):
            stat1 = stats[i] + stats[j] + stats[k]
            stat2 = total_stats - stat1
            diff = abs(stat1 - stat2)
            min_diff = min(min_diff, diff)
print(min_diff)