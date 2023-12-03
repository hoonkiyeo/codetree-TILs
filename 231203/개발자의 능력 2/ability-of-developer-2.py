stats = list(map(int, input().split()))
n = 6

min_diff = 99999999
for i in range(n):
    for j in range(i+1, n):
        team1 = stats[i] + stats[j]
        for k in range(n):
            for l in range(k+1, n):
                if k != i and k != j and l != i and l != j:
                    team2 = stats[k] + stats[l]
                    team3 = sum(stats) - team1 - team2
                    
                    max_stat = max(team1, team2, team3)
                    min_stat = min(team1, team2, team3)
                    diff = max_stat - min_stat
                    min_diff = min(min_diff, diff)
print(min_diff)