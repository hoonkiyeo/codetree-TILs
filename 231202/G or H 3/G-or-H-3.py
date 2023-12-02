n,k = map(int, input().split())
positions = [0] * 10001
for _ in range(n):
    pos, letter = input().split()
    pos = int(pos)
    positions[pos] = 1 if letter == 'G' else 2

max_score = 0
for i in range(1, k+1):
    score = 0
    for j in range(i, i+k+1):
        score += positions[j]
    max_score = max(max_score, score)
print(max_score)