n,k = map(int, input().split())
positions = [0] * 10001
max_num = 0
for _ in range(n):
    pos, letter = input().split()
    pos = int(pos)
    positions[pos] = 1 if letter == 'G' else 2
    max_num = max(pos, max_num)

if k > max_num:
    print(sum(positions))
else:
    max_score = 0
    for i in range(1, max_num-k+1):
        score = 0
        score += sum(positions[i:i+k+1])
        max_score = max(max_score, score)
    print(max_score)