n,k = map(int, input().split())
arr = []
for i in range(n):
    arr.append(input().split())
    arr[i][0] = int(arr[i][0])

placed = [0] * 10001 
for ele in arr:
    if ele[1] == 'G':
        placed[ele[0]] = 1
    elif ele[1] == 'H':
        placed[ele[0]] = 2

max_score = 0
for i in range(1, k+1):
    score = 0
    for j in range(i, i+k+1):
        score += placed[j]
    max_score = max(max_score, score)
print(max_score)