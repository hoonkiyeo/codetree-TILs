n = int(input())
trials = []
for _ in range(n):
    a,b,c = map(int, input().split())
    trials.append((a,b,c))

max_score = 0
for i in range(1,4):
    score = 0
    arr = [0] * 4
    arr[i] = 1
    for a,b,c in trials:
        arr[a], arr[b] = arr[b], arr[a]
        if arr[c] == 1:
            score += 1
    max_score = max(max_score, score)
print(max_score)