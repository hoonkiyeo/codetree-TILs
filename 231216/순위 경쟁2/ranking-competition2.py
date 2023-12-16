n = int(input())
scores = []
for _ in range(n):
    c,s = input().split()
    s = int(s)
    scores.append((c,s))

p,s = scores[0]
score_a = 0
score_b = 0
if p == 'A':
    score_a += s
elif p == 'B':
    score_b += s
if score_a > score_b:
    prev_winner = 'A'
else:
    prev_winner = 'B'

cnt = 1
for i in range(1,n):
    p, s = scores[i]
    if p == 'A':
        score_a += s
    elif p == 'B':
        score_b += s
    if score_a > score_b:
        winner = 'A'
    elif score_a < score_b:
        winner = 'B'
    else:
        winner = 'AB'
    if winner != prev_winner:
        prev_winner = winner
        cnt += 1
print(cnt)