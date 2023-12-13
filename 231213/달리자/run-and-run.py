n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

total_dist = 0
move = 0
for i in range(n):
    diff = A[i] - B[i]
    move += diff

    if move > 0:
        total_dist += move

print(total_dist)