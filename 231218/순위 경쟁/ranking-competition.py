n = int(input())
scores = []
for _ in range(n):
    c,s = input().split()
    s = int(s)
    scores.append((c,s))

cnt = 0
score_a = 0
score_b = 0
score_c = 0
prev_winner = 'ABC'
for i in range(n):
    p,s = scores[i]
    # 어떤 학생인지 판단
    if p == 'A':
        score_a += s
    elif p == 'B':
        score_b += s
    elif p == 'C':
        score_c += s
    # 점수 계산
    if score_a > score_b and score_a > score_c:
        winner = 'A'
    elif score_a < score_b and score_b > score_c:
        winner = 'B'
    elif score_c > score_a and score_c > score_b:
        winner = 'C'
    elif score_a == score_b and score_a > score_c:
        winner = 'AB'
    elif score_a == score_c and score_a > score_b:
        winner = 'AC'
    elif score_b == score_c and score_b > score_a:
        winner = 'BC'
    else:
        winner = 'ABC'
    # 만약 winner가 바뀌었다면 cnt + 1
    if winner != prev_winner:
        prev_winner = winner
        cnt += 1
print(cnt)