n = 5
stats = list(map(int, input().split()))
min_diff = 99999999
is_possible = False

for i in range(n):
    for j in range(i+1, n):
        team1 = stats[i] + stats[j]
        for k in range(n):
            for l in range(k+1, n):
                if k != i and k != j and l != i and l != j:
                    team2 = stats[k] + stats[l]
                    team3 = sum(stats) - team1 - team2

                    if team1 != team2 and team1 != team3 and team2 != team3:
                        max_score = max(team1, team2, team3)
                        min_score = min(team1, team2, team3)
                        diff = max_score - min_score
                        min_diff = min(min_diff, diff)
                        is_possible = True

if is_possible:
    print(min_diff)
else:
    print(-1)